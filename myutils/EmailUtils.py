import smtplib

from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

from myutils.CommonConfig import *

conf = CommonConfig()


def send_email(send_from, send_to, subject, text, files=None, server="smtp.exmail.qq.com"):
    # assert(isinstance(send_to,list),"Send To email should be a list")

    mail_user = conf.config['mail_user']
    mail_pass = conf.config['mail_pass']

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = send_to
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(text, 'html'))

    with open(files, "rb") as f:
        part = MIMEApplication(f.read(), Name=basename(files))
        msg.attach(part)

    smtp = smtplib.SMTP_SSL(server, 465)
    smtp.login(mail_user, mail_pass)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.quit()


def send_report(files):
    send_f = conf.config['mail_user']
    send_t = conf.config['send_to']

    subject = "[Automaiton]TestReport_" + str(datetime.today())

    files = files
    with open(files, 'r') as f:
        text = f.read()

    send_email(send_f, send_t, subject, text, files)
