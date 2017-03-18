#sending mail through gmail via python
import getpass
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import os

class ServerMail():
    """docstring for mailServer"""
    def login(self):
        self.gmail_user = raw_input("Your gmail id: ")
        self.gmail_pwd = getpass.getpass('Password for %s: ' % self.gmail_user)
   
    def mail_service(self):
        self.to = raw_input("Reciever gmail id: ")
        self.subject = raw_input("Subject: ")
        self.body = raw_input("Body: ")

        attachment = raw_input("Do you want to attach a file(Y/n): ")
        if attachment=='Y' or attachment=='y':
            self.attach_file = raw_input("File name: ")
        else:
            self.attach_file=None
        
    def send_mail(self):
        msg = MIMEMultipart()
        msg['From'] = self.gmail_user
        msg['To'] = self.to
        msg['Subject'] = self.subject
        msg.attach(MIMEText(self.body,'plain'))

        if self.attach_file:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(open(self.attach_file, 'rb').read())
            Encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(self.attach_file))
            msg.attach(part)

        try:
            mailServer = smtplib.SMTP("smtp.gmail.com", 587)
            mailServer.ehlo()
            mailServer.starttls()
            mailServer.ehlo()
            mailServer.login(self.gmail_user, self.gmail_pwd)
            mailServer.sendmail(self.gmail_user, self.to, msg.as_string())
            mailServer.quit()
            print 'Successfully sent the mail'
        except Exception as e:
            raise e
            print 'Failed to send the mail'

def main():
    m = ServerMail()
    m.login()
    m.mail_service()
    m.send_mail()

if __name__ == '__main__':
    main()
