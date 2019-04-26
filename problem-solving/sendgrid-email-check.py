import sendgrid
import os
from sendgrid.helpers.mail import *
api_key='api_key'
sg = sendgrid.SendGridAPIClient(apikey=api_key)
from_email = Email("email")
to_email = Email("To_mail")
subject = "Sending with SendGrid is Fun"
content = Content("text/plain", "and easy to do anywhere, even with Python")
mail = Mail(from_email, subject, to_email, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)