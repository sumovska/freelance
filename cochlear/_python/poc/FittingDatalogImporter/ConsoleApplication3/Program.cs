using System;
using System.Linq;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;
using Cochlear.CustomSound.DataAccessLayer.Interop;
using Cochlear.CustomSound.DataAccessLayer.Interop.Crf;
using Cochlear.CustomSound.DataAccessLayer.Interop.Interfaces;

namespace POC
{
    class Program
    {
        private DataAccessEngine engine;
        private CrfGuidGenerator _guidGenerator;

        static void Main(string[] args)
        {
            // It doesn't actually make sense to exclude these...
            // Why should the CRF implant's implant ID have a higher priority than that of a non-crf implant id?
            // Unless we change the GUID implant namespace.
            bool excludeCrfImplants = false;
            
            var metadata = new Metadata(
                // Clinician and Surgeon names and emails are ignored by the import process...
                // (They're relevant only for MH's UI)
                "Clinician", "Clinician@Clinic", "Surgeon", "Surgeon@Surgery",
                new Recipient {
                    NameFirst = "Charlie",
                    NameLast = "Chaplain",
                    DateBirth = new DateTime(1889, 4, 16),
                    Gender = 'M'
                },
                new Implant {
                    ImplantResistorId = "154321",
                    DateImplantation = DateTime.Now.Date,
                    DateExplantation = DateTime.Now.Date,
                    SerialNo = "123412341234",
                    FkPart = 51001,
                    ELocus = Implant.ImplantLocus.Left
                },
                new Implant {
                    ImplantResistorId = "765432",
                    DateImplantation = DateTime.Now.Date,
                    DateExplantation = DateTime.Now.Date,
                    SerialNo = "123412341234",
                    FkPart = 51001,
                    ELocus = Implant.ImplantLocus.Right
                });

            new Program().Run(
                excludeCrfImplants,
                metadata,
                args);
        }

        public Program()
        {
            this.engine = new DataAccessEngine();
            // Should consider a custom CrfGuidGenerator that uses a Crf2-specific namespace,
            // so that CRF and CRF2 implants can be distinguished.
            this._guidGenerator = new CrfGuidGenerator();
        }

        void Run(bool excludeCrfImplants, Metadata metadata, string[] crfFiles)
        {
            var implants = ToList(
                metadata.ImplantForLocus(Implant.ImplantLocus.Left),
                metadata.ImplantForLocus(Implant.ImplantLocus.Right)).ToArray();

            
            if (ExistingRecipientsHaveDuplicateImplantIds(excludeCrfImplants, implants))
            {
                return;
            }
            var recipient = FuzzyLocateRecipient(metadata.Recipient);
            AlterRecipient(recipient, metadata);
            ImportRecipient(crfFiles, implants);
        }

        private Recipient FuzzyLocateRecipient(Recipient recipient)
        {
            // Obviously, this is a simple proof of concept...
            var list = new RecipientList();
            var exampleRecipientQuery = new Recipient();
            exampleRecipientQuery.ImplantCollection.Add(new Implant());
            this.engine.FetchDataObjectList(list, exampleRecipientQuery);
            foreach(var ido in list)
            {
                var rec = ido as Recipient;
                if (rec.NameFirst == recipient.NameFirst
                    || rec.NameLast == recipient.NameLast
                    || rec.DateBirth == recipient.DateBirth)
                {
                    Console.WriteLine("{0} {1} {2} has been selected. Existing implants on the same side of the new implant will be explanted", recipient.NameFirst, recipient.NameLast, recipient.DateBirth);
                    return rec;
                }
            }
            recipient.NewGuidRecipientGuid();
            Console.WriteLine("Could not locate recipient, a new recipient will be created");
            this.engine.SaveDataObject(recipient);
            return recipient;
        }

        private void AlterRecipient(Recipient recipient, Metadata metadata)
        {
            // First explant any that already exist on that locus...
            // Unless, of course, it is imported as a result of the CRF(2) import...
            foreach (var ido in recipient.ImplantCollection) {
                var implant = ido as Implant;
                if (implant.GuidImplant == this._guidGenerator.GenerateImplantGuid(implant.ImplantResistorId)) {
                    // Import process will use this implant directly, avoiding the need for the DAL to do
                    // orphan implant matching up.
                    continue;
                }
                if (implant.EStatus != Implant.ImplantStatus.Implanted)
                {
                    continue;
                }
                var newImplant = metadata.ImplantForLocus(implant.ELocus);
                if (newImplant != null)
                {
                    implant.DateExplantation = newImplant.DateImplantation;
                    ExplantImplant(implant);
                }
            }

            foreach (var locus in new Implant.ImplantLocus[] { Implant.ImplantLocus.Left, Implant.ImplantLocus.Right })
            {
                var implant = metadata.ImplantForLocus(locus);
                CreateAndSaveImplant(recipient, implant);
            }
        }

        private void CreateAndSaveImplant(Recipient recipient, Implant implant)
        {
            implant.GuidImplant = this._guidGenerator.GenerateImplantGuid(implant.ImplantResistorId);
            var implantList = new ImplantList();
            this.engine.FetchDataObjectList(implantList, implant);
            if (implantList.Count > 0)
            {
                // Hmm, we already have the implant in the database.
                // Assume that it's a the same implant, and don't change it.
                Console.WriteLine("Not creating a new implant: This implant already exists (ID: {0})", implant.ImplantResistorId);
                return;
            }
            implant.FkGuidRecipient = recipient.GuidRecipient;
            implant.EStatus = Implant.ImplantStatus.Implanted;
            engine.SaveDataObject(implant);
            Console.WriteLine("Created new implant for import (ID: {0})", implant.ImplantResistorId);
            recipient.ImplantCollection.Add(implant);
            engine.SaveDataObject(recipient);
        }

        private void ExplantImplant(Implant implant)
        {
            implant.EStatus = Implant.ImplantStatus.Explanted;
            Console.WriteLine("Implant ID {0}, Locus {1} explanted", implant.ImplantResistorId, implant.ELocus.ToString());
            engine.SaveDataObject(implant);
        }

        private List<string> ToList(Implant left, Implant right)
        {
            var implants = new List<string>();
            if (left != null) { implants.Add(left.ImplantResistorId); }
            if (right != null) { implants.Add(right.ImplantResistorId); }
            return implants;
        }

        private bool ExistingRecipientsHaveDuplicateImplantIds(bool excludeCrfImplants, string[] implants)
        {
            var recipients = RecipientsWithImplants(excludeCrfImplants, implants);
            if (recipients.Count > 0)
            {
                Console.WriteLine("Woe is you!  A recipient in your database already has the implant ID you are importing, please fix it (In Custom Sound)");
                Console.Write("(These recipients are ");
                foreach (var rec in recipients)
                {
                    Console.Write("{0} {1}, ", rec.NameFirst, rec.NameLast);
                }
                Console.Write("\b\b\n");
            }
            return recipients.Count > 0;
        } 
        

        private IList<Recipient> RecipientsWithImplants(bool excludeCrfImplants, string[] implants)
        {
            var matched = new List<Recipient>();
            var recipients = new RecipientList();
            var exampleRecipientQuery = new Recipient();
            exampleRecipientQuery.ImplantCollection.Add(new Implant());
            this.engine.FetchDataObjectList(recipients, exampleRecipientQuery);
            foreach (var ido_rec in recipients)
            {
                var rec = ido_rec as Recipient;
                foreach (var ido_implant in rec.ImplantCollection)
                {
                    var implant = ido_implant as Implant;
                    if (implants.Contains(implant.ImplantResistorId))
                    if (!excludeCrfImplants || implant.GuidImplant != this._guidGenerator.GenerateImplantGuid(implant.ImplantResistorId))
                    {
                        matched.Add(rec);
                        break;
                    }
                }
            }
            return matched;
        }

        IWirelessAssistantXmlImportResult[] ImportRecipient(string[] crfFiles, string[] implants)
        {
            var results = new List<IWirelessAssistantXmlImportResult>();
            foreach (var crf in crfFiles)
            {
                var xmlData = System.IO.File.ReadAllText(crf, Encoding.UTF8);
                var guidGenerator = this._guidGenerator;
                var parser = new CrfParser(
                    guidGenerator,
                    new MangledImplantIdPreprocessor(implants),
                    new TimeStampPreprocessor(),
                    new NrtDataPreprocessor(),
                    new ReadImpedancesParser(guidGenerator),
                    new ObjectiveThresholdsParser(guidGenerator, new ObjectiveThresholdSummaryGenerator()),
                    new ElectrodeFlaggingParser(),
                    new NrtParser(guidGenerator),
                    new UnrecoverableDataPreprocessor(),
                    new NrtProgramGuidPreprocessor());

                var importer = new WirelessAssistantXmlImporter(engine, parser, new RemoveDuplicationFromImplantsCommand(engine));
                results.Add(importer.Import(xmlData, this.OnProgress));
            }
            return results.ToArray();
        }

        private void OnProgress(int arg1, int arg2)
        {
            Console.WriteLine("{0}, {1}", arg1, arg2);
        }
    }
}
