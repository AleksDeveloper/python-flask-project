import emailUtils
import os
from dotenv import load_dotenv
load_dotenv()
from cryptography.fernet import MultiFernet

# key = b'TVGwqvsXqyKauWPU1hMTGIqziHidncYeaOgnioYeiW8='
# key2 = bytes(os.getenv("MY_ENCRYPTION_KEY"), "utf-8")
# print(type(key2))
# print(key2)
# print(type(os.getenv("MY_ENCRYPTION_KEY")))
# password = os.getenv("MY_ENCRYPTED_PASSWORD")
# print(key, password)

# my_password = emailUtils.decrypt_string(key2, password)
my_email = os.getenv("MY_OUTLOOK_EMAIL")
my_password = os.getenv("MY_OUTLOOK_PASSWORD")

# emailUtils.send_email_mul_att(my_email, my_password, ['aliecama@gmail.com', 'aliecama@hotmail.com', 'pythontesteract@outlook.com'], 'Test from emailUtils', 'Hello my friend', [['../icon.png', 'icon.png', 'image', 'png'],
#                     ['../Dockerfile', 'Dockerfile', 'application', 'json'],
#                       ['../Jenkinsfile', 'Jenkinsfile', 'application', 'json']])

htmlmessage = """\
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       How are you?<br>
       Here is the <a href="http://www.python.org">link</a> for getting 999,999,999 recognition points for being a good leader.<br>
       With this points, you can buy a Tesla.<br>
       Regards,<br>
       Julie Sweet & Jeff Bezos.
    </p>
  </body>
</html>
"""
emailUtils.send_email_as_html(my_email, my_password, ['alejandro.carrillo@accenture.com'], 'Test as HTML', htmlmessage, ['../static/uploads/COX - Shadowing topics.txt'])
