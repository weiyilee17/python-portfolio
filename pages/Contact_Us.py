from streamlit import header, form, text_input, text_area, form_submit_button, info
from practice.send_email import send_email

header('Contact Me')

with form(key='contactForm'):
    user_email = text_input('Your email address')
    user_message = text_area('Your message')

    message_sent = f"""\
Subject: New email from {user_email}

From: {user_email}
{user_message}
"""

    submit_button_pressed = form_submit_button(label='Submit')

    if submit_button_pressed:
        send_email(message_sent)
        info('Your email was sent successfully.')
