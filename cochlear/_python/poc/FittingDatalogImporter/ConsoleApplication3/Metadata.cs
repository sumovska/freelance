using Cochlear.CustomSound.DataAccessLayer.Interop;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace POC
{
    public class Metadata
    {
        private Recipient _recipient;
        private Implant[] _implant;

        public Metadata(
            string clinicName, string clinicEmail, string surgeonName, string surgenEmail,
            Recipient recipient,
            params Implant[] implants)
        {
            this._recipient = recipient;
            this._implant = implants;
        }

        public Implant ImplantForLocus(Implant.ImplantLocus locus)
        {
            foreach (Implant implant in this._implant)
            {
                if (implant.ELocus == locus)
                {
                    return implant;
                }
            }
            return null;
        }

        public Recipient Recipient { get; set; }
    }
}
