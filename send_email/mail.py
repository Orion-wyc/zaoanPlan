from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from .configuration import email_info, to_addr
import smtplib

sender_user = email_info["sender_user"]
sender_pwd = email_info["sender_pwd"]
smtp_server = email_info["smtp_server"]


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def send_email(content):
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['From'] = _format_addr(sender_user)
    msg['To'] = _format_addr(to_addr)
    msg['Subject'] = Header('zaoan plan', 'utf-8').encode()

    server = smtplib.SMTP(smtp_server, )
    server.set_debuglevel(1)
    server.login(sender_user, sender_pwd)
    for i in range(len(to_addr)):
        server.sendmail(sender_user, to_addr[i], msg.as_string())
    server.quit()


if __name__ == "__main__":
    print(sender_user)
