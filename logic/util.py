# util.py

import logging
from dotenv import load_dotenv, get_key
import os

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

# CROMEDRIVER_PATH = '/usr/local/bin/chromedriver'

# login
USER = get_key(dotenv_path, 'USER')
PASSWORD = get_key(dotenv_path, 'PASSWORD')
URL = get_key(dotenv_path, 'URL')
PASSWORD_XPATH = '//*[@id="password"]'
LOGIN_XPATH = '//*[@id="loginBtn"]/span'

# data extraction
DETAILS = 'div.rt-tbody'
EXTRACT_PATH = '/Volumes/Samsung 970 EVO/Documents/Python/livevox_date_checker/details.csv'
OUTPUT_PATH = '/Volumes/Samsung 970 EVO/Documents/Python/livevox_date_checker/output.txt'

# email sending
GMAIL_APP_PASSWORD = get_key(dotenv_path, 'GMAIL_APP_PASSWORD')
SENDER_EMAIL = get_key(dotenv_path, 'SENDER_EMAIL')
RECEIVER_EMAIL = get_key(dotenv_path, 'RECEIVER_EMAIL')

# logging
LOG_OUTPUT = '/Volumes/Samsung 970 EVO/Documents/Python/livevox_date_checker/log.txt'
LOG_LEVEL = logging.INFO