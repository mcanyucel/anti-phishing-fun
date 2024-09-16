from selenium.webdriver.chrome.webdriver import WebDriver as ChromeWebDriver
from selenium.webdriver.common.by import By
from driver import create_chromium_driver
from helpers import generate_random_email, find_element_by_xpath, generate_invalid_credit_card_number, generate_random_variable_string, generate_random_month, generate_random_year, generate_random_integer
from tqdm import tqdm
import time
from timeit import default_timer as  timer


"""
This file targets a phishing for the below target url
"""

# Initial configuration
headless = False
targetUrl = "https://irp.cdn-website.com/02ccf804/files/uploaded/webpage.html"
numberOfRecords = 1
recordCounter = 0


startTime = timer()

print("\nA total of {} records defined for target site {}\n".format(numberOfRecords, targetUrl))

browser: ChromeWebDriver = create_chromium_driver(headless=headless)
for i in tqdm(range(numberOfRecords), desc="Adding records"):
    browser.get(targetUrl)
    time.sleep(4)
    
    emailControl = find_element_by_xpath(browser, "//*[@id='id_userLoginId']")
    emailControl.send_keys(generate_random_email())
    
    passwordControl = find_element_by_xpath(browser, "//*[@id='id_password']")
    passwordControl.send_keys(generate_random_variable_string(4, 32, True))
    
    signInControl = find_element_by_xpath(browser, "//*[@id='appMountPoint']/div/div[3]/div/div/div[1]/form/button")
    signInControl.click()
    
    time.sleep(6)
    
    restartMembershipButton = find_element_by_xpath(browser, '//*[@id="appMountPoint"]/div/div/div[2]/div/a/div/button')
    restartMembershipButton.click()
    
    time.sleep(6)
    
    cardNameControl = find_element_by_xpath(browser, '//*[@id="id_lastName"]')
    name = f"{generate_random_variable_string(3, 12)} {generate_random_variable_string(5, 12)}"
    cardNameControl.send_keys(name)
    
    cardNumberControl = find_element_by_xpath(browser, '//*[@id="id_creditCardNumber"]')
    cardNumberControl.send_keys(generate_invalid_credit_card_number)
    
    cardDateControl = find_element_by_xpath(browser, '//*[@id="id_creditExpirationMonth"]')
    cardDateControl.send_keys(f"{generate_random_month}{generate_random_year}")
    
    cardCVVControl = find_element_by_xpath(browser, '//*[@id="id_creditCardSecurityCode"]')
    cardCVVControl.send_keys(generate_random_integer(100, 999))
    
    startMembershipButton = find_element_by_xpath(browser, '//*[@id="appMountPoint"]/div/div/div[2]/div/form/div[2]/button')
    startMembershipButton.click()
    
    time.sleep(10)
    recordCounter = recordCounter + 1
    
browser.close()

endTime = timer()

print("A total of {} records are inserted in {} seconds.\n".format(numberOfRecords, endTime - startTime))
