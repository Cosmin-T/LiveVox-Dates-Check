# main.py

import time
from logic.webdriver import *
from logic.login import *
from logic.navigation import *
from logic.details import *
from logic.email_send import *
from logic.flag import *
from logic.logs import *

conf_log()

if __name__ == '__main__':
    try:
        driver = initialize_webdriver(URL)
        log(driver)
        nav(driver)
        time.sleep(5)
        det(driver)
        check_date()

        if check_and_set_flag():
            send_email()

    except Exception as e:
        print(f'Exception: {e}')
