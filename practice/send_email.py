from smtplib import SMTP_SSL
from ssl import create_default_context
from os import getenv


def send_email(message):
    host = 'smtp.gmail.com'
    port = 465
    username = getenv('EMAIL_SENDER')
    password = getenv('PORTFOLIO_APP_PASSWORD')
    receiver = getenv('EMAIL_RECEIVER')
    context = create_default_context()

    with SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

