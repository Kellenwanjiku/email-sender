#go over to our gmail account and setup 2 factor authentication
#generate app password

from email.message import EmailMessage
import ssl
import smtplib

#create a function to send the mail
email_sender = 'kellenwanjikugitahi@gmail.com'
email_password = 'kunj lllu djxg vvzm'

email_receiver = 'fosagi3266@usoplay.com'

subject = "Dont forget to subscribe"
body = """
When you watch a video, please hit subscribe
"""
#create instance of library that we imported and its EmailMessage above

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp: 
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())





