from email.message import EmailMessage
from flask import flash
import smtplib
from cryptography.fernet import Fernet
from mimetypes import guess_type
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def encrypt_string(key, plaintext):
    fernet_key = Fernet(key)
    encrypted_text = fernet_key.encrypt(plaintext.encode())
    return encrypted_text.decode()

def decrypt_string(key, encrypted_text):
    fernet_key = Fernet(key)
    decrypted_text = fernet_key.decrypt(encrypted_text.encode())
    return decrypted_text.decode()

def send_email_sing_att(sender, senderPassword, recipient, subject, message, attachmentPath, fileName, mainType, subType):
    email = EmailMessage()
    email["From"] = sender
    email["To"] = recipient
    email["Subject"] = subject
    email.set_content(message)
    
    with open(attachmentPath, "rb") as f:
        email.add_attachment(
            f.read(),
            filename = fileName,
            maintype = mainType,
            subtype = subType
        )
    
    smtp = smtplib.SMTP("smtp-mail.outlook.com", port=587)
    smtp.starttls()
    smtp.login(sender, senderPassword)
    smtp.sendmail(sender, recipient, email.as_string())
    smtp.quit()

def send_email_mul_att(sender, senderPassword, recipient, subject, message, attachments):
    email = EmailMessage()
    email["From"] = sender
    email["To"] = recipient
    email["Subject"] = subject
    email.set_content(message)
    
    for list in attachments:
        with open(list, "rb") as f:
            print("AQUI MARCO ERROR:",str(guess_type(str(list))))
            email.add_attachment(
                f.read(),
                filename = str(list.rsplit('/', 1)[-1]),
                maintype = str(guess_type(str(list))).split('/')[0],
                subtype = str(guess_type(str(list))).split('/')[1]
            )
    try:
        smtp = smtplib.SMTP("smtp-mail.outlook.com", port=587)
        smtp.starttls()
        smtp.login(sender, senderPassword)
        smtp.sendmail(sender, recipient, email.as_string())
        smtp.quit()
        return "OK"
    except smtplib.SMTPAuthenticationError as e:
        return str(e)
    
def send_email_as_html(sender, senderPassword, recipient, subject, htmlmessage, attachments):
    email = EmailMessage()
    email['Subject'] = subject
    email['From'] = sender
    email['To'] = recipient
    email.add_header('Content-Type', 'text/html')
    email.set_payload(htmlmessage)

    for list in attachments:
       with open(list, "rb") as f:
            print("AQUI MARCO ERROR:",str(guess_type(str(list))))
            email.add_attachment(
                f.read(),
                filename = str(list.rsplit('/', 1)[-1]),
                maintype = "application",
                subtype = "octet-stream"
                # maintype = str(guess_type(str(list))).split('/')[0],
                # subtype = str(guess_type(str(list))).split('/')[1]
            )
    try:
        smtp = smtplib.SMTP("smtp-mail.outlook.com", port=587)
        smtp.starttls()
        smtp.login(sender, senderPassword)
        smtp.sendmail(sender, recipient, email.as_string())
        smtp.quit()
        return "OK"
    except smtplib.SMTPAuthenticationError as e:
        return str(e)
    except smtplib.SMTPDataError as e:
        return str(e)
    except smtplib.SMTPConnectError as e:
        return str(e)
    except smtplib.SMTPNotSupportedError as e:
        return str(e)
