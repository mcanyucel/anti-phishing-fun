from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def create_chromium_driver(headless: bool):
    service = Service('/usr/bin/chromedriver') # Default location; change if necessary
    
    chrome_options = Options()
    chrome_options.binary_location = "/usr/bin/chromium"  # Default location; change if necessary

    if headless:
        chrome_options.add_argument('--headless')
        
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    return driver