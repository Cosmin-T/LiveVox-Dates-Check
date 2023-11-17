# details.py

import time
import os
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import pandas as pd
from logic.util import *
import logging
from logic.logs import *

conf_log()

def det(driver):
    try:
        # Fetch the text using the CSS selector
        entire_text = driver.find_element(By.CSS_SELECTOR, DETAILS).text
        split_text = entire_text.split("\n")

        # Splitting data into groups of 4 (filename, type, size, date)
        grouped_data = []
        for i in range(0, len(split_text), 4):
            group = split_text[i:i+4]
            grouped_data.append(group)

        # Transforming data to the desired format
        transformed_data = []
        for group in grouped_data:
            if len(group) == 4:
                filename, size, file_type, date = group
                row = [filename, file_type, size, date]
                transformed_data.append(row)

        # Convert to DataFrame
        df = pd.DataFrame(transformed_data, columns=["filename", "type", "size", "date"])
        logging.info('Dataframe created')

        # Write to CSV
        df.to_csv(EXTRACT_PATH, index=False)
        logging.info('Dataframe written to CSV')


    except Exception as e:
        logging.error(f'Exception: {e}')

def check_date():
    today = datetime.now().strftime('%m/%d/%Y')

    # Check the last modification date of OUTPUT_PATH
    if os.path.exists(OUTPUT_PATH):
        last_modified_date = datetime.fromtimestamp(os.path.getmtime(OUTPUT_PATH)).strftime('%m/%d/%Y')
        if last_modified_date != today:
            with open(OUTPUT_PATH, 'w') as out_file:
                out_file.write('')  # Clear the content
        else:
            # Append a space after each run if the file already exists and it's the same day
            with open(OUTPUT_PATH, 'a') as out_file:
                out_file.write('\n')

    try:
        with open(EXTRACT_PATH, 'r') as f:
            lines = f.readlines()
            if not lines:
                logging.info("The file is empty.")

            for line in lines:
                if line.startswith('ABC') or line.startswith('DRAGON') or line.startswith('AGA'):
                    if ',"' not in line:
                        logging.info(f"Found a line with ABC, DRAGON, or AGA but no , : {line.strip()}")
                        continue

                    parts = line.split(',"')
                    name = parts[0].split(',')[0].strip()
                    date_and_time = parts[1].strip('"')
                    table_date = date_and_time.split(',')[0].strip()

                    with open(OUTPUT_PATH, 'a') as out_file:  # 'a' mode appends to the file
                        if table_date == today:
                            logging.info(f"{name}: {table_date} == {today} - OK")
                            out_file.write(f"{name}: {table_date} == {today} - OK\n")
                        else:
                            logging.info(f"{name}: {table_date} != {today} - FAIL")
                            out_file.write(f"{name}: {table_date} != {today} - FAIL\n")

    except Exception as e:
        logging.error(f'Exception: {e}')
