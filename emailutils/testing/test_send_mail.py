import pytest
import smtplib
import email.message
from unittest.mock import MagicMock, patch
from emailutils.emailUtils import send_email_as_html

@pytest.fixture
def mock_email_message():
    with patch('email.message.EmailMessage') as mock_email_message:
        yield mock_email_message.return_value

@pytest.fixture
def mock_open():
    with patch('builtins.open', create=True) as mock_open:
        yield mock_open

@pytest.fixture
def mock_smtplib():
    with patch('smtplib.SMTP') as mock_smtplib:
        smtp_instance = mock_smtplib.return_value
        smtp_instance.starttls.return_value = None
        smtp_instance.login.return_value = None
        yield smtp_instance

def test_send_email_as_html(mock_email_message, mock_open, mock_smtplib):
    # Mock the open function to return a mock file object
    mock_file = MagicMock(spec=open)
    mock_file.__enter__.return_value.read.return_value = b'Test attachment data'
    mock_open.return_value = mock_file

    sender = 'your_email@example.com'
    sender_password = 'your_password'
    recipient = 'recipient@example.com'
    subject = 'Test Subject'
    html_message = '<html><body><h1>Hello, World!</h1></body></html>'
    attachments = ['/path/to/attachment1.txt', '/path/to/attachment2.jpg']

    result = send_email_as_html(sender, sender_password, recipient, subject, html_message, attachments)

    assert result == "OK"
    mock_email_message.assert_called_once()
    mock_file.assert_called_with('/path/to/attachment1.txt', 'rb')
    mock_file.assert_called_with('/path/to/attachment2.jpg', 'rb')
    mock_smtplib.SMTP.assert_called_once_with("smtp-mail.outlook.com", port=587)
    mock_smtplib.SMTP.return_value.starttls.assert_called_once()
    mock_smtplib.SMTP.return_value.login.assert_called_once_with(sender, sender_password)
    mock_smtplib.SMTP.return_value.sendmail.assert_called_once_with(sender, recipient, MagicMock().as_string())
    mock_smtplib.SMTP.return_value.quit.assert_called_once()

if __name__ == '__main__':
    pytest.main()


