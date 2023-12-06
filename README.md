# LiveVox-Dates-Check

**IMPORTANT:** This serves as an informative repository with no need for installation, as there is no `config.ini` file, and the automation is designed for a specific website inaccessible to anyone.

## Modules

### webdriver.py

- Initializes a headless Chrome WebDriver using Selenium.
- Navigates to a specified URL.
- Handles exceptions and logs errors.
- Returns the WebDriver instance for further use.

### login.py

- Provides functions for logging into the website.
- Uses Selenium to fill in login credentials and click the login button.
- Logs login-related actions and errors.

### navigation.py

- Implements navigation and interaction with web elements.
- Uses Selenium to click on specific elements and navigate through the website.
- Logs navigation-related actions and errors.

### details.py

- Retrieves and processes details from the website.
- Extracts and transforms data into a desired format.
- Writes data to CSV files.
- Checks dates and updates existing files.
- Logs details-related actions and errors.

### flag.py

- Manages a flag file to determine whether to send email notifications.
- Checks for the existence of the flag file and sets it for the second run.
- Logs flag-related actions and errors.

### email_send.py

- Sends email notifications with reports as attachments.
- Configures email content and attachments.
- Sends emails using SMTP.
- Logs email sending actions and errors.

### logs.py

- Configures and initializes the logging system.
- Sets the log level, format, and log file path.
- Used to log actions and errors throughout the script.

### main.py

- Orchestrates the execution of the script.
- Imports and utilizes modules to perform the following tasks:
  1. Initializes the Chrome WebDriver.
  2. Logs into the website.
  3. Navigates through web pages.
  4. Retrieves and processes inventory details.
  5. Checks and sets a flag for email notifications.
  6. Sends email notifications if the flag is set.
  7. Handles exceptions and errors.

## Configuration

The script may rely on configuration settings stored in a separate configuration file or within each module. These settings include:

- URLs for websites to scrape data from.
- Chrome WebDriver executable path.
- Login credentials.
- XPaths for web elements to interact with.
- File paths for data storage and reports.
- Logging settings (log level and log file path).
