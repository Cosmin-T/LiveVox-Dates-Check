from logic.util import *
from logic.logs import *
import logging
from datetime import datetime, time
import datetime as dt

conf_log()

from playwright.sync_api import Playwright, sync_playwright, expect
import time

def get_data(page):
    """
    Extracts the data from the LiveVox page and writes it to a file

    Parameters:
    page (playwright.sync_api.Page): The page to extract the data from
    """
    try:
        # Clear the output file
        with open(OUTPUT_PATH, 'w') as f:
            f.write('')

        # Get the data from the page
        details = page.inner_text(DETAILS)
        lines = details.strip().split('\n')

        # Create a list of lists, where each sublist contains 4 lines of data
        list_of_lists = []
        for i in range(0, len(lines), 4):
            sublist = lines[i:i+4]
            list_of_lists.append(sublist)

        # Iterate over each sublist and extract the data
        for sublist in list_of_lists:
            file_name = sublist[0].split('.')[0]
            date = sublist[-1]

            # Skip the DailyDNC file as it is not relevant
            if file_name == "DailyDNC":
                continue

            # Parse the date and time from the string
            date_object = dt.datetime.strptime(date, "%m/%d/%Y, %H:%M:%S")

            # Get the current date and time
            today_date = dt.datetime.now().date()
            after_time = dt.datetime.combine(today_date, dt.time(7, 35))

            # Check if the file loaded correctly
            if date_object.date() == today_date and date_object.time() < after_time.time():
                # Write the file name and date to the output file
                with open(OUTPUT_PATH, 'a') as f:
                    f.write(f'{file_name}\n')
                    f.write(f'{date} | Loaded correctly on {today_date} before {after_time}\n\n')

            else:
                # Write the file name and date to the output file
                with open(OUTPUT_PATH, 'a') as f:
                    f.write(f'{file_name}\n')
                    f.write(f'{date} | Failed to load on {today_date} before {after_time}\n')

        logging.info('Data Extracted')

    except Exception as e:
        logging.error(f'Error: {e}')

def run(playwright: Playwright) -> None:
    """
    Navigates to the LiveVox page, logs in, and extracts the data

    Parameters:
    playwright (playwright.sync_api.Playwright): The Playwright object
    """
    browser = playwright.webkit.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(30000)

    try:
        page.goto(URL)
        logging.info('URL Inserted')

        # Fill in the username and password
        page.locator("#username").click()
        page.locator("#username").fill(USER)
        logging.info('Username Inserted')

        page.locator("#password").click()
        page.locator("#password").fill(PASSWORD)
        logging.info('Password Inserted')

        # Click the login button
        page.locator("#password").press("Enter")
        logging.info('Logged In')

        # Wait for the page to load
        time.sleep(5)

        # Click the Configure button
        page.get_by_role("button", name="Configure").click()
        logging.info('Configured Pressed')

        # Expand the Input/Output tree item and click the AddBoxIcon
        page.get_by_role("treeitem", name="Input / Output").get_by_test_id("AddBoxIcon").click()
        logging.info('Input/Output Expanded')

        # Select the SFTP Browser
        page.locator("#ftpBrowser").get_by_text("SFTP Browser").click()
        logging.info('SFTP Selected')

        # Expand the root directory of the SFTP Browser
        page.get_by_role("treeitem", name="/", exact=True).locator("span").first.click()
        logging.info('SFTP Expanded')

        # Select the contactDone file
        page.get_by_role("treeitem", name="contactDone").locator("span").nth(3).click()
        logging.info('ContactDone Selected')

        # Wait for the file to load
        time.sleep(1)

    except Exception as e:
        logging.error(f'Error: {e}')

    # Extract the data from the page
    get_data(page)
