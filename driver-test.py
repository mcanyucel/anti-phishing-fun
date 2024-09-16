from selenium.webdriver.chrome.webdriver import WebDriver as ChromeWebDriver
from driver import create_chromium_driver

driver: ChromeWebDriver = create_chromium_driver(headless=False)
try:
    driver.get("https://www.google.com")
    print(driver.title)
    # Keep the browser open until user input
    input("Press Enter to close the browser...")
finally:
    driver.quit()
