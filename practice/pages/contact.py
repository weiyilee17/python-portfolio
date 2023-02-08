from streamlit import form, form_submit_button, text_input, text_area, selectbox, info
from pandas import read_csv

from practice.send_email import send_email

discuss_topics = read_csv(filepath_or_buffer='practice/topics.csv')


with form(key='contact_form'):
    user_email = text_input('Your Email Address')
    topic = selectbox('What topic do you want to discuss?', discuss_topics)
    user_text = text_area('Text')

    message_sent = f"""\
Subject: New email from {user_email}

From: {user_email}
Topic: {topic}

{user_text}
"""

    submit_button_pressed = form_submit_button(label='Submit')

    if submit_button_pressed:
        send_email(message_sent)
        info('Your email was sent successfully.')