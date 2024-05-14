from logic.util import *
from logic.navigation import *

if __name__ == '__main__':
    with sync_playwright() as playwright:
        run(playwright)