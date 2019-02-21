# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# import smtplib
#
# # create message object instance
# msg = MIMEMultipart()
#
# message = "Thank you"
#
# # setup the parameters of the message
# password = "prasad27$"
# msg['From'] = "prasanna.kumar@news.co.uk"
# msg['To'] = "prasanna.kumar@news.co.uk"
# msg['Subject'] = "Subscription"
#
# # add in the message body
# msg.attach(MIMEText(message, 'plain'))
#
# # create server
# server = smtplib.SMTP('143.252.81.3:25')
# #smtp_port = 25
# server.starttls()
#
# # Login Credentials for sending the mail
# server.login(msg['From'], password)
#
# # send the message via the server.
# server.sendmail(msg['From'], msg['To'], msg.as_string())
#
# server.quit()
# quit
# print ("successfully sent email")


# import smtplib, ssl
#
# port = 25  # For starttls
# smtp_server = "143.252.81.3"
# sender_email = "prasanna.kumar@news.co.uk"
# receiver_email = "prasanna.kumar@news.co.uk"
# password = "prasad27$"
# message = """\
# Subject: Hi there
#
# This message is sent from Python."""
#
# context = ssl.create_default_context()
# with smtplib.SMTP(smtp_server, port) as server:
#     server.ehlo()  # Can be omitted
#     server.starttls(context=context)
#     server.ehlo()  # Can be omitted
#     server.login(sender_email, password)
#     server.sendmail(sender_email, receiver_email, message)



# import smtplib, ssl
#
# port = 587  # For starttls
# smtp_server = "smtp.gmail.com"
# sender_email = "prasanna55kt@gmail.com"
# receiver_email = "prasanna55kt@gmail.com"
# password = "prasad596600"
# message = """\
# Subject: Hi there
#
# This message is sent from Python."""
#
# context = ssl.create_default_context()
# with smtplib.SMTP(smtp_server, port) as server:
#     #server.ehlo()  # Can be omitted
#     server.starttls(context=context)
#     #server.ehlo()  # Can be omitted
#     server.login(sender_email, password)
#     server.sendmail(sender_email, receiver_email, message)


# import smtplib
# # set up the SMTP server
# s = smtplib.SMTP(host='smtp.gmail.com', port=587)
# s.starttls()
# s.login("prasanna55kt@gmail.com", "prasad596600")


import smtplib
# set up the SMTP server
s = smtplib.SMTP(host='143.252.81.3', port=25)
s.starttls()
s.login("prod-d2p@news.co.uk", "Newsuk@datatech_blr23")