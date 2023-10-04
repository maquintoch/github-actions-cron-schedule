import smtplib
import ssl
import os


port = 465
smtp_Server = "smtp.gmail.com"
UserName = os.environ.get('USER_EMAIL')
Password = os.environ.get('USER_PASSWORD')
message = """\
Subject: GitHub Email Report

This is your daily report from Login server..
Author: 
Year: 2023
    """

context = ssl.create_default_context
with smtplib.SMTP_SSL(smtp_Server, port, context=context) as server:
    server.login(UserName, Password)
    server.sendmail(UserName, UserName, message)
