#! /usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import getpass

browser = webdriver.Chrome()
browser.get('http://www.citimortgage.com')
userBox = browser.find_element_by_name('username')
userBox.send_keys('jasondixon5')
pwBox = browser.find_element_by_name('password')

pw = getpass.getpass('Enter pw: ')

pwBox.send_keys(pw)
pwBox.submit()
statementsLink = browser.find_element_by_link_text('view statements')
statementsLink.click()

#dropdown = browser.find_element_by_xpath("//select[@id='years']")
#dropdown.click()
#dropdown.send_keys(Keys.DOWN)
#dropdown.click()

dropdown = browser.find_element_by_xpath("//option[2]")
#Option 1 is blank, option 2 is current year
dropdown.click()

try:
    mar_inv = browser.find_element_by_partial_link_text('Mar')
except:
    print('not found')
    
mar_inv.click()

try:
    feb_inv = browser.find_element_by_partial_link_text('Feb')
except:
    print('not found')

feb_inv.click()