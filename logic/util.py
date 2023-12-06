# util.py

import logging
from logic.config_ini import *

config = con()

# webdriver
URL = config['DEFAULT']['URL']
CROMEDRIVER_PATH = '/usr/local/bin/chromedriver'

# login
USER = config['DEFAULT']['USER']
USER_XPATH = '//*[@id="username"]'
PASSWORD = config['DEFAULT']['PASSWORD']
PASSWORD_XPATH = '//*[@id="password"]'
LOGIN_XPATH = '//*[@id="loginBtn"]/span'

# naviation
CONFIGURE_XPATH = '//*[@id="lv-app"]/div/div/div/aside/div/div/div[2]/ul/button[1]'
INPUT_OUTPUT_XPATH = '//*[@id="inOut"]/div/div[2]/div'
SFTP = '//*[@id="ftpBrowser"]/div/div[2]/div'
EXPAND = '//*[@id="lv-app"]/div/div/div/section/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div[2]/div/div/ul/li/span[1]'
CONTACTDONE = '//*[@id="lv-app"]/div/div/div/section/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div[2]/div/div/ul/li/ul/li[3]/span[2]/span[2]'

# data extraction
ABC = '//*[@id="lv-app"]/div/div/div/section/div/div[2]/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/div[1]'
DNS = '//*[@id="lv-app"]/div/div/div/section/div/div[2]/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/div[2]'
AGA = '//*[@id="lv-app"]/div/div/div/section/div/div[2]/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/div[3]'
DETAILS = 'div.rt-tbody'
EXTRACT_PATH = '/Volumes/Samsung 970 EVO/Documents/Python/livevox_date_checker/details.csv'
OUTPUT_PATH = '/Volumes/Samsung 970 EVO/Documents/Python/livevox_date_checker/output.txt'

# email sending
SENDER_EMAIL = config['DEFAULT']['SENDER_EMAIL']
RECEIVER_EMAIL = config['DEFAULT']['RECEIVER_EMAIL']
GMAIL_APP_PASSWORD = config['DEFAULT']['GMAIL_APP_PASSWORD']

# flaging to ensure it can send the email
FLAG_OUTPUT = '/Volumes/Samsung 970 EVO/Documents/Python/livevox_date_checker/flag_output.txt'

# logging
LOG_OUTPUT = '/Volumes/Samsung 970 EVO/Documents/Python/livevox_date_checker/log.txt'
LOG_LEVEL = logging.INFO