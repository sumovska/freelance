using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Cochlear.CustomSound.DataAccessLayer.Interop.Crf;
using System.Xml.Linq;
using System.Text.RegularExpressions;

namespace POC
{
    class MangledImplantIdPreprocessor : IImplantIdPreprocessor
    {
        private string[] implants;
        public MangledImplantIdPreprocessor(string[] implants)
        {
            this.implants = implants;
        }

        public void InsertImplantIds(XDocument xmlDocument)
        {
            var elements = xmlDocument.Descendants();

            var implantId = "";
            foreach(var el in elements)
            {
                implantId = el.Name.LocalName == "measure_implant_id" ? el.Attribute("implantid").Value : implantId;
                SetImplantId("measure_impedance", el, implantId);
                SetImplantId("measure_nrt_trace", el, implantId);
                SetImplantId("read_impedances", el, implantId);
                //// No need to insert implantid's in profile_plus and diagnostics elements as they already have implantid in the xml
            };
        }

        public void RemoveElementsForImplantsWithInvalidIds(XDocument document)
        {
            var elements = document.Descendants();
            var elementsToRemove = new List<XElement>();

            foreach (var el in elements) { 
                var implantId = el.Attribute("implantid");
                if (implantId == null)
                {
                    continue;
                }

                if (!implants.Contains(implantId.Value))
                {
                    elementsToRemove.Add(el);
                }
            }

            elementsToRemove.ForEach(x => x.Remove());
        }

        private static void SetImplantId(string elementName, XElement el, string implantId)
        {
            if (el.Name.LocalName == elementName)
            {
                el.SetAttributeValue("implantid", implantId);
            }
        }
    }
}
