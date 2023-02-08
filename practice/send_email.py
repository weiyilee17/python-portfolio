from smtplib import SMTP_SSL
from ssl import create_default_context
from os import getenv


def send_email(message):
    host = 'smtp.gmail.com'
    port = 465
    username = 'weiyilee17@gmail.com'
    password = getenv('PASSWORD')
    receiver = username
    context = create_default_context()

    with SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

