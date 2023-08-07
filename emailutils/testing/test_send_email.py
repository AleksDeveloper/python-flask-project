import smtplib
import pytest
from unittest.mock import MagicMock, patch, call
from emailutils.emailUtils import send_email_as_html
from os import environ

@pytest.fixture
def mock_smtp():
    with patch('smtplib.SMTP') as mock_smtp:
        smtp_instance = mock_smtp.return_value
        smtp_instance.starttls.return_value = None
        smtp_instance.login.return_value = None
        yield smtp_instance

# def test_send_email_successfully(mock_smtp):
#     sender = environ.get("MY_OUTLOOK_EMAIL")
#     sender_password = environ.get("MY_OUTLOOK_PASSWORD")
#     recipient = 'recipient@example.com'
#     subject = 'Test Subject'
#     html_message = '<html><body><h1>Hello my friend</h1></body></html>'
#     attachments = ['../../static/uploads/Izzi.pdf', '../../static/uploads/Inventario.xlsx']

#     result = send_email_as_html(sender, sender_password, recipient, subject, html_message, attachments)

#     assert result == "OK"
#     expected_calls = [
#         call(sender, recipient, MagicMock().as_string())
#     ]
#     #mock_smtp.sendmail.assert_called_once_with(sender, recipient, MagicMock().as_string())
#     mock_smtp.sendmail.assert_has_calls(expected_calls)
#     mock_smtp.quit.assert_called_once()

def test_send_email_authentication_error(mock_smtp):
    sender = 'alejandro.carrillo@example.com'
    sender_password = 'wrong_password'
    recipient = 'recipient@example.com'
    subject = 'Test Subject'
    html_message = '<html><body><h1>Hello my friend</h1></body></html>'
    attachments = ['../../static/uploads/Izzi.pdf', '../../static/uploads/Inventario.xlsx']

    mock_smtp.login.side_effect = smtplib.SMTPAuthenticationError(535, 'Authentication Failed.')
    print(mock_smtp)

    result = send_email_as_html(sender, sender_password, recipient, subject, html_message, attachments)
    print(result)
    print(type(result))

    assert result == "(535, 'Authentication Failed.')"
    mock_smtp.quit.assert_called_once()

