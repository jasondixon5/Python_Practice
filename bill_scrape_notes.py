try:
    elem = browser.find_element_by_class_name('bookcover')
    print('Found <{}> element with that class name!'.format(elem.tag_name))
except:
    print('Was not able to find an element with that name.')
    
    
linkElem = browser.find_element_by_link_text('Read It Online')
type(linkElem)
linkElem.click() #follows the "Read it online" link

emailElem = browser.find_element_by_name("Email")

>>> from selenium import webdriver
>>> browser = webdriver.Chrome()
>>> browser.get('http://www.gmail.com')
>>> box = browser.find_element_by_name('Email')
>>> box.send_keys('jasondixonmail@gmail.com')
>>> box.submit()
>>> import getpass
>>> pw = getpass.getpass('Enter pw: ')
Enter pw: 

pwBox = browser.find_element_by_name('Passwd')
>>> pwBox.send_keys(pw)
>>> pwBox.submit()
>>> 
browser.close()


CitiMortgage
>>> browser = webdriver.Chrome()
>>> browser.get('http://www.citimortgage.com')
>>> userBox = browser.find_element_by_id('username')
>>> userBox = browser.find_element_by_name('username')
>>> userBox.send_keys('jasondixon5')
>>> pwBox = browser.find_element_by_name('password')
>>> import getpass
>>> pw = getpass.getpass('Enter pw: ')
Enter pw: 
>>> pwBox.send_keys(pw)
>>> pwBox.submit()
>>> statementsLink = browser.find_element_by_link_text('view statements')
>>> statementsLink.click()

current = browser.find_element_by_partial_link_text('RetrieveNewStatement')

<a href="#" title="Select and open the statement you wish to view, print or save." oncontextmenu="return disableselect()" onclick="tagLinkSC(this, 'Current| MortgSum|Statement',{'eVar33': 'PDF','eVar32': 'Current Statement','eVar3': 'Document Request'});return openPDFBillingStatement('RetrieveNewStatement.do',7, 0, 9163082399402485383,'Monthly Statement','statements','EN');"> Mar 2016 (PDF) </a>