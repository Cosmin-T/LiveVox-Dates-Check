# email_send.py

import smtplib
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from logic.util import *
import logging
from logic.logs import *

conf_log()

def send_email():
    today = datetime.now().strftime('%m/%d/%Y')

    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL
    msg['Subject'] = f'Daily LiveVox Date Check - {today}'

    body = f'Please check the daily LiveVox date check for {today} at: \n{URL}'
    msg.attach(MIMEText(body, 'plain'))

    try:
        with open(OUTPUT_PATH, 'rb') as f:
            attachment = MIMEApplication(f.read(), _subtype='txt')
            attachment.add_header('content-Disposition', 'attachment', filename='output.txt')
            msg.attach(attachment)

        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.login(SENDER_EMAIL, GMAIL_APP_PASSWORD)
            smtp.send_message(msg)
            logging.info("Email sent successfully!")

    except Exception as e:
        logging.error(f'Exception: {e}')