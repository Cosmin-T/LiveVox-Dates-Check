# login.py

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logic.util import *
import logging
from logic.logs import *

conf_log()

def log(driver):
    try:
        search_user = driver.find_element(By.XPATH, USER_XPATH)
        search_user.send_keys(USER)
        logging.info('User Added')
        search_user = driver.find_element(By.XPATH, PASSWORD_XPATH)
        search_user.send_keys(PASSWORD)
        logging.info('Password Added')
        login_btn = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, LOGIN_XPATH)))
        login_btn.click()
        logging.info('Next Clicked')

        time.sleep(1)

    except Exception as e:
        logging.error(f'Error: {e}')