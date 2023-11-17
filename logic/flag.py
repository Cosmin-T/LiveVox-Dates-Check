# flag.py

import os
import logging
from logic.logs import *
from logic.util import *

conf_log()

def check_and_set_flag():
    if os.path.exists(FLAG_OUTPUT):
        os.remove(FLAG_OUTPUT)
        logging.info("Flag removed")
        return True  # Indicate that the email should be sent (second run)
    else:
        with open(FLAG_OUTPUT, 'w') as f:
            f.write("Flag set for second run.")
            logging.info("Flag set for second run")
        return False  # Indicate this is the first run and email should not be sent