import smtplib
import time

From = "hethong@vnptepay.com.vn"
To = ["khanhnn@vnptepay.com.vn"]
Date = time.ctime(time.time())
Subject = "New message."
Text = "Message Text"
#Format mail message
mMessage = ('From: %s\nTo: %s\nDate: \
            %s\nSubject: %s\n%s\n' %
            (From, To, Date, Subject, Text))

print 'Connecting to Server'
s = smtplib.SMTP('mail.vnptepay.com.vn')

rCode = s.sendmail(From, To, mMessage)
s.quit()

if rCode:
    print 'Error Sending Message'
else:
    print 'Message Sent Successfully'