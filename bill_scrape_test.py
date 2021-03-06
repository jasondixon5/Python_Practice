#! /usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import getpass

browser = webdriver.Chrome()
browser.get('https://www.georgiapower.com/')

signInButton = browser.find_element_by_link_text('My Account Login')
signInButton.click()

driver.switch_to_frame(driver.find_element_by_tag_name("iframe"))

"""Found info about switching frames here:
https://stackoverflow.com/questions/7534622/selecting-an-iframe-using-python-selenium/24286392#24286392?newreg=a3ce99758d064a388f39830fb70d854c
"""

element = driver.find_element_by_id('ctl00_MainContent_txtUsername')
element.send_keys('nroget')

element = driver.find_element_by_id('ctl00_MainContent_txtPassword')
pw = getpass.getpass('Enter pw: ')
element.send_keys(pw)

element = driver.find_element_by_id('ctl00_MainContent_btnLogin')
element.click()
driver.switch_to_default_content()

#Open most recent invoice in new window
element = driver.find_element_by_id('ctl00_MainContent_PayBillControl_A1')
element.click()

