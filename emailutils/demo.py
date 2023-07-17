import os
import win32com.client as win32

#Construct Outlook app instance
olApp = win32.Dispatch('Outlook.Application')
olNS = olApp.GetNameSpace('MAPI')

#Construct the email item object
mailItem = olApp.CreateItem(0)
mailItem.Subject = "Dummy Email"
mailItem.BodyFormat = 1
mailItem.Body = "Hello, this is Raheem Sterling, king of Nigeria. Please give me your funds for this new webapp"
mailItem.To = 'ricardo.a.perez@accenture.com; jesus.rosas@accenture.com;'
#attachments
mailItem.Attachments.Add(os.path.join(os.getcwd(), '../icon.png'))
mailItem.Attachments.Add(os.path.join(os.getcwd(), '../Jenkinsfile'))
mailItem.Attachments.Add(os.path.join(os.getcwd(), '../Dockerfile'))

mailItem.Display()
mailItem.Send()