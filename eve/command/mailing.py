#sending mail through gmail via python
import getpass
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import os
import subprocess
# import tkinter as tk
# from tkinter import filedialog

import note


class ServerMail():
    """docstring for mailServer"""
    def login(self):
        subprocess.call(['say', 'Who is the sender?'])
        self.gmail_user = raw_input("Enter your gmail id: ")
        self.gmail_pwd = getpass.getpass('Password for %s: ' % self.gmail_user)
   
    def mail_service(self):
        subprocess.call(['say', 'Who is the receiver?'])
        self.to = raw_input("Receiver gmail id: ")
        subprocess.call(['say', 'What is the subject?'])
        self.subject = raw_input("Subject: ")

        subprocess.call(['say', 'Tell me what to write'])
        self.body = note.main().capitalize()

        subprocess.call(['say', 'Do you want to attach a file?'])
        attachment = note.main()
        if attachment.lower().startswith('y'):
            # root = tk.Tk()
            # root.withdraw()
            # self.file_path = filedialog.askopenfilename()
            self.file_path = raw_input("Enter file name: ")
        else:
            self.file_path = None
        
    def send_mail(self):
        msg = MIMEMultipart()
        msg['From'] = self.gmail_user
        msg['To'] = self.to
        msg['Subject'] = self.subject
        msg.attach(MIMEText(self.body,'plain'))

        if self.file_path:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(open(self.file_path, 'rb').read())
            Encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(self.file_path))
            msg.attach(part)

        try:
            mailServer = smtplib.SMTP("smtp.gmail.com", 587)
            mailServer.ehlo()
            mailServer.starttls()
            mailServer.ehlo()
            mailServer.login(self.gmail_user, self.gmail_pwd)
            mailServer.sendmail(self.gmail_user, self.to, msg.as_string())
            mailServer.quit()
            return 'Successfully sent'
        except:
            return 'Failed to send'

def main():
    m = ServerMail()
    m.login()
    m.mail_service()
    return m.send_mail()

if __name__ == '__main__':
    main()
