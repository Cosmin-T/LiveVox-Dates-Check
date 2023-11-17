# navigation.py

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logic.util import *
import logging
from logic.logs import *

conf_log()

def nav(driver):
    try:

        navigator_list = [
            lambda: WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, CONFIGURE_XPATH))),
            lambda: WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, INPUT_OUTPUT_XPATH))),
            lambda: WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, SFTP))),
            lambda: WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, EXPAND))),
            lambda: WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, CONTACTDONE)))
        ]

        for nav_func in navigator_list:
            nav_func().click()

        if nav_func():
            print_list = ['Clicked Configure', 'Clicked Input/Output', 'Clicked SFTP',
                    'Clicked Expand', 'Clicked Contact Done']
            for prnt in print_list:
                logging.info(prnt)
        else:
            logging.error(f'Error clicking: {prnt}')


    except Exception as e:
        logging.error(f'Error: {e}')