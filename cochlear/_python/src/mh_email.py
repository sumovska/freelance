import boto.ses
import boto.sns
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import logging
from Queue import Queue
from threading import Thread
from constants import AWS_KEY_ID, AWS_SECRET, AWS_EMAILS_REGION
import time

log = logging.getLogger(__name__)

DEFAULT_SENDER = 'cr220dataviewer@cochlear.com'

class MagicHatEmail(Thread):
    def __init__(self):
        super(MagicHatEmail, self).__init__()
        self._mails = Queue()
        self._errors = Queue()
        self._die = False;
        
    def run(self):
        log.info("Started MagicHatEmail thread")
        while not self._die:
            time.sleep(0.5)
            
            if not self._mails.empty():
                self._conn = boto.ses.connect_to_region(
                    AWS_EMAILS_REGION,
                    aws_access_key_id=AWS_KEY_ID,
                    aws_secret_access_key=AWS_SECRET)
                    
            while not self._mails.empty():
                try:
                    log.info(self._conn.send_raw_email(self._mails.get(), DEFAULT_SENDER))
                    self._log_queue_status()
                except Exception, e:
                    self._errors.put(e)
            
    def die(self):
        self._die = True;
            
    def send_sessions(self, sessions):
        for session in sessions:
            self.send(**session)
        
    def send(self, targets, replyto, subject, body, attachments):
        log.info("send(%s, %s, %s, %s, ...)", targets, replyto, subject, body)
        msg = MIMEMultipart()
        msg['Subject'] = 'Test Email'
        msg['From'] = DEFAULT_SENDER
        msg['Reply-To'] = replyto
        msg['To'] = ', '.join(targets)
        msg.preamble = 'You will not see this in a MIME-aware mail reader.\n'
        
        body = MIMEText(body)
        msg.attach(body)
        
        for filename, data in attachments:
            maintype, subtype = 'application/octet-stream'.split('/')
            attach = MIMEBase(maintype, subtype)
            attach.set_payload(data)
            encoders.encode_base64(attach)
            attach.add_header('Content-Disposition', 'attachment', filename=filename)
            msg.attach(attach)
        
        self._mails.put(msg.as_string())
        self._log_queue_status()
        
    def get_errors(self):
        if not self._errors.empty():
            return self._errors.get()
    
    def _log_queue_status(self):
        log.info('There are now %d items in the mail queue', self._mails.qsize())
        