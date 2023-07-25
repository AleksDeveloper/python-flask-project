from email.message import EmailMessage
import smtplib
from os import environ

sender = environ.get('MY_OUTLOOK_EMAIL')
password = environ.get('MY_OUTLOOK_PASSWORD')
recipient = "aliecama@hotmail.com"
subject = "Test email with SMTP and Outlook from Python"
message = "Hello World!, now attaching a file to this"


attachmentsList = {['../icon.png', 'icon.png', 'image', 'png'],
                    ['../Dockerfile', 'Dockerfile', 'application', 'json'],
                      ['../Jenkinsfile', 'Jenkinsfile', 'application', 'json']}

email = EmailMessage()
email["From"] = sender
email["To"] = recipient
email["Subject"] = subject
email.set_content(message)
with open("../icon.png", "rb") as f:
    email.add_attachment(
        f.read(),
        filename="icon.png",
        maintype="image",
        subtype="png"
    )

smtp = smtplib.SMTP("smtp-mail.outlook.com", port=587)
smtp.starttls()
smtp.login(sender, password)
smtp.sendmail(sender, recipient, email.as_string())
smtp.quit()