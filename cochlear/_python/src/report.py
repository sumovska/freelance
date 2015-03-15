from base64 import b64encode
import json
from encoders import JsonEncoder
from cStringIO import StringIO
from xhtml2pdf.pisa import pisaDocument
import sys

HTML_TEMPLATE = """
<html>
  <head>
    <title>{name_first} {name_last}</title>
  </head>
  <body>
  <h1>{name_first} {name_last}</h1>
  
  <table>
  <tr>
    <th>Date</th>
    <th>Serial</th>
    <th>DOB</th>
    <th>Gender</th>
    <th>Surgery</th>
    <th>Surgeon</th>
    <th>Clinic</th>
  </tr>
  <tr>
    <td>{local_date}</td>
    <td>{implant_serial}</td>
    <td>{dob}</td>
    <td>{gender}</td>
    <td>{surgery}</td>
    <td>{surgeon}</td>
    <td>{clinic}</td>
  </tr>
  </table>

  <h2>Impedances</h2>
  (impedances_chart)

  <h2>NRT Profile</h2>
  (nrt_profile_chart)

  </body>
</html>
"""


class ReportException(Exception):
    pass


class Image(object):
    def __init__(self, png_data):
        self._pngdata = png_data

    def html(self):
        return '<img src="data:image/png;base64,' + b64encode(self._pngdata) + '">'


class Report(object):
    def __init__(self, dataset):
        data = dataset[0]
        # Sanity check:
        d = data.keys()
        for item in HTML_TEMPLATE.split("{")[1:]:
            k = item.split("}", 1)[0]
            if k not in d:
                raise ReportException("{k} not found in data".format(k=k))

        self._data = {}
        for k, v in data.items():
            if isinstance(v, Image):
                self._data[k] = v.html()
            elif v:
                self._data[k] = v
            else:
                self._data[k] = 'empty'


    def html(self):
        return HTML_TEMPLATE.format(raw=json.dumps(self._data, cls=JsonEncoder), **self._data)

    def pdf(self):
        fsrc = StringIO(self.html())

        r = pisaDocument(
            fsrc,
            fdest=None,
            debug=0,
            path=None,
            errout=sys.stdout,
            tempdir=None,
            format="pdf",
            link_callback=None,
            default_css=None,
            xhtml=False,
            encoding=None,
            xml_output=None).dest
        return r.getvalue()

    def save_pdf(self, location):
        try:
            with open(location, 'wb') as f:
                f.write(self.pdf())
        except:
            # Try again!
            with open(location, 'wb') as f:
                f.write(self.pdf())