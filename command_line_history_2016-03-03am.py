Last login: Wed Mar  2 19:04:50 on ttys001
Jasons-MacBook-Air:~ jasondixon$ python3
Python 3.5.1 (v3.5.1:37a07cee5969, Dec  5 2015, 21:12:44) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from selenium import webdriver
>>> from selenium.webdriver.common.keys import Keys
>>> import getpass
>>> 
>>> browser = webdriver.Chrome()
>>> browser.get('https://www.georgiapower.com/')
>>> signInButton = browser.find_element_by_class('login')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'WebDriver' object has no attribute 'find_element_by_class'
>>> signInButton = browser.find_element_by_class_name('login')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 378, in find_element_by_class_name
    return self.find_element(by=By.CLASS_NAME, value=name)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 712, in find_element
    {'using': by, 'value': value})['value']
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 201, in execute
    self.error_handler.check_response(response)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/errorhandler.py", line 194, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"class name","selector":"login"}
  (Session info: chrome=49.0.2623.75)
  (Driver info: chromedriver=2.20.353124 (035346203162d32c80f1dce587c8154a1efa0c3b),platform=Mac OS X 10.11.3 x86_64)

>>> signInButton = browser.find_element_by_xpath("//div[@class='logins']")

^CTraceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 258, in find_element_by_xpath
    return self.find_element(by=By.XPATH, value=xpath)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 712, in find_element
    {'using': by, 'value': value})['value']
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 199, in execute
    response = self.command_executor.execute(driver_command, params)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/remote_connection.py", line 395, in execute
    return self._request(command_info[0], url, body=data)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/remote_connection.py", line 426, in _request
    resp = self._conn.getresponse()
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/http/client.py", line 1174, in getresponse
    response.begin()
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/http/client.py", line 282, in begin
    version, status, reason = self._read_status()
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/http/client.py", line 243, in _read_status
    line = str(self.fp.readline(_MAXLINE + 1), "iso-8859-1")
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/socket.py", line 575, in readinto
    return self._sock.recv_into(b)
KeyboardInterrupt
>>> signInButton = browser.find_element_by_xpath("//div[@class='logins']")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 258, in find_element_by_xpath
    return self.find_element(by=By.XPATH, value=xpath)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 712, in find_element
    {'using': by, 'value': value})['value']
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 199, in execute
    response = self.command_executor.execute(driver_command, params)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/remote_connection.py", line 395, in execute
    return self._request(command_info[0], url, body=data)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/remote_connection.py", line 425, in _request
    self._conn.request(method, parsed_url.path, body, headers)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/http/client.py", line 1083, in request
    self._send_request(method, url, body, headers)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/http/client.py", line 1118, in _send_request
    self.putrequest(method, url, **skips)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/http/client.py", line 951, in putrequest
    raise CannotSendRequest(self.__state)
http.client.CannotSendRequest: Request-sent
>>> signInButton = browser.find_element_by_link_text('My Account Login')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 282, in find_element_by_link_text
    return self.find_element(by=By.LINK_TEXT, value=link_text)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 712, in find_element
    {'using': by, 'value': value})['value']
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 199, in execute
    response = self.command_executor.execute(driver_command, params)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/remote_connection.py", line 395, in execute
    return self._request(command_info[0], url, body=data)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/remote_connection.py", line 425, in _request
    self._conn.request(method, parsed_url.path, body, headers)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/http/client.py", line 1083, in request
    self._send_request(method, url, body, headers)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/http/client.py", line 1128, in _send_request
    self.endheaders(body)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/http/client.py", line 1079, in endheaders
    self._send_output(message_body)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/http/client.py", line 911, in _send_output
    self.send(msg)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/http/client.py", line 854, in send
    self.connect()
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/http/client.py", line 826, in connect
    (self.host,self.port), self.timeout, self.source_address)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/socket.py", line 711, in create_connection
    raise err
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/socket.py", line 702, in create_connection
    sock.connect(sa)
ConnectionRefusedError: [Errno 61] Connection refused
>>> browser = webdriver.Chrome()
browser.get('https://www.georgiapower.com/')
>>> browser.get('https://www.georgiapower.com/')
>>> signInButton = browser.find_element_by_link_text('My Account Login')
>>> 
>>> signInButton.click()
>>> userBox = browser.find_element_by_xpath("//*[@id='ctl00_MainContent_spanUsernameTextbox']
  File "<stdin>", line 1
    userBox = browser.find_element_by_xpath("//*[@id='ctl00_MainContent_spanUsernameTextbox']
                                                                                            ^
SyntaxError: EOL while scanning string literal
>>> ")
  File "<stdin>", line 1
    ")
     ^
SyntaxError: EOL while scanning string literal
>>> userBox = browser.find_element_by_xpath("//*[@id='ctl00_MainContent_spanUsernameTextbox']")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 258, in find_element_by_xpath
    return self.find_element(by=By.XPATH, value=xpath)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 712, in find_element
    {'using': by, 'value': value})['value']
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 201, in execute
    self.error_handler.check_response(response)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/errorhandler.py", line 194, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"xpath","selector":"//*[@id='ctl00_MainContent_spanUsernameTextbox']"}
  (Session info: chrome=49.0.2623.75)
  (Driver info: chromedriver=2.20.353124 (035346203162d32c80f1dce587c8154a1efa0c3b),platform=Mac OS X 10.11.3 x86_64)

>>> userBox = browser.find_element_by_id('#ctl00_MainContent_spanUsernameTextbox')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 234, in find_element_by_id
    return self.find_element(by=By.ID, value=id_)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 712, in find_element
    {'using': by, 'value': value})['value']
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 201, in execute
    self.error_handler.check_response(response)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/errorhandler.py", line 194, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"id","selector":"#ctl00_MainContent_spanUsernameTextbox"}
  (Session info: chrome=49.0.2623.75)
  (Driver info: chromedriver=2.20.353124 (035346203162d32c80f1dce587c8154a1efa0c3b),platform=Mac OS X 10.11.3 x86_64)

>>> userBox = browser.find_element_by_id('ctl00_MainContent_spanUsernameTextbox')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 234, in find_element_by_id
    return self.find_element(by=By.ID, value=id_)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 712, in find_element
    {'using': by, 'value': value})['value']
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 201, in execute
    self.error_handler.check_response(response)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/errorhandler.py", line 194, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"id","selector":"ctl00_MainContent_spanUsernameTextbox"}
  (Session info: chrome=49.0.2623.75)
  (Driver info: chromedriver=2.20.353124 (035346203162d32c80f1dce587c8154a1efa0c3b),platform=Mac OS X 10.11.3 x86_64)

>>> userBox = browser.find_element_by_id('ctl00_MainContent_spanUsername')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 234, in find_element_by_id
    return self.find_element(by=By.ID, value=id_)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 712, in find_element
    {'using': by, 'value': value})['value']
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 201, in execute
    self.error_handler.check_response(response)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/errorhandler.py", line 194, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"id","selector":"ctl00_MainContent_spanUsername"}
  (Session info: chrome=49.0.2623.75)
  (Driver info: chromedriver=2.20.353124 (035346203162d32c80f1dce587c8154a1efa0c3b),platform=Mac OS X 10.11.3 x86_64)

>>> userBox
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'userBox' is not defined
>>> userBox = browser.find_element_by_id("ctl00_MainContent_spanUsernameTextbox")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 234, in find_element_by_id
    return self.find_element(by=By.ID, value=id_)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 712, in find_element
    {'using': by, 'value': value})['value']
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 201, in execute
    self.error_handler.check_response(response)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/errorhandler.py", line 194, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"id","selector":"ctl00_MainContent_spanUsernameTextbox"}
  (Session info: chrome=49.0.2623.75)
  (Driver info: chromedriver=2.20.353124 (035346203162d32c80f1dce587c8154a1efa0c3b),platform=Mac OS X 10.11.3 x86_64)

>>> userBox = browser.find_element_by_xpath("//input[@name='ctl00$MainContent$txtUsername']")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 258, in find_element_by_xpath
    return self.find_element(by=By.XPATH, value=xpath)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 712, in find_element
    {'using': by, 'value': value})['value']
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 201, in execute
    self.error_handler.check_response(response)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/errorhandler.py", line 194, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"xpath","selector":"//input[@name='ctl00$MainContent$txtUsername']"}
  (Session info: chrome=49.0.2623.75)
  (Driver info: chromedriver=2.20.353124 (035346203162d32c80f1dce587c8154a1efa0c3b),platform=Mac OS X 10.11.3 x86_64)

>>> userBox = browser.find_element_by_xpath("//input[@name='ctl00$MainContent$txtUsername']")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 258, in find_element_by_xpath
    return self.find_element(by=By.XPATH, value=xpath)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 712, in find_element
    {'using': by, 'value': value})['value']
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 201, in execute
    self.error_handler.check_response(response)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/errorhandler.py", line 194, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"xpath","selector":"//input[@name='ctl00$MainContent$txtUsername']"}
  (Session info: chrome=49.0.2623.75)
  (Driver info: chromedriver=2.20.353124 (035346203162d32c80f1dce587c8154a1efa0c3b),platform=Mac OS X 10.11.3 x86_64)

>>> 
>>> 
>>> ?
  File "<stdin>", line 1
    ?
    ^
SyntaxError: invalid syntax
>>> XZ
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'XZ' is not defined
>>> userBox = browser.find_element_by_name('ctl00$MainContent$txtUsername')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 330, in find_element_by_name
    return self.find_element(by=By.NAME, value=name)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 712, in find_element
    {'using': by, 'value': value})['value']
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 201, in execute
    self.error_handler.check_response(response)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/errorhandler.py", line 194, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"name","selector":"ctl00$MainContent$txtUsername"}
  (Session info: chrome=49.0.2623.75)
  (Driver info: chromedriver=2.20.353124 (035346203162d32c80f1dce587c8154a1efa0c3b),platform=Mac OS X 10.11.3 x86_64)

>>> userBox = browser.find_elements_by_name('ctl00$MainContent$txtUsername')
>>> userBox.text
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute 'text'
>>> def(userBox)
  File "<stdin>", line 1
    def(userBox)
       ^
SyntaxError: invalid syntax
>>> dev(userBox)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'dev' is not defined
>>> userBox
[]
>>> userBox = browser.find_elements_by_name('ctl00$MainContent$txtUsername')
>>> userBox = browser.find_element_by_name('ctl00$MainContent$txtUsername')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 330, in find_element_by_name
    return self.find_element(by=By.NAME, value=name)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 712, in find_element
    {'using': by, 'value': value})['value']
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 201, in execute
    self.error_handler.check_response(response)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/errorhandler.py", line 194, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"name","selector":"ctl00$MainContent$txtUsername"}
  (Session info: chrome=49.0.2623.75)
  (Driver info: chromedriver=2.20.353124 (035346203162d32c80f1dce587c8154a1efa0c3b),platform=Mac OS X 10.11.3 x86_64)

>>> browser.window_handles
['CDwindow-FE5E1003-C2A6-4FEB-97C7-68258B7D05FC']
>>> browser.switch_to_window(browser.window_handles[0])
>>> userBox = browser.find_element_by_name('ctl00$MainContent$txtUsername')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 330, in find_element_by_name
    return self.find_element(by=By.NAME, value=name)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 712, in find_element
    {'using': by, 'value': value})['value']
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 201, in execute
    self.error_handler.check_response(response)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/errorhandler.py", line 194, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"name","selector":"ctl00$MainContent$txtUsername"}
  (Session info: chrome=49.0.2623.75)
  (Driver info: chromedriver=2.20.353124 (035346203162d32c80f1dce587c8154a1efa0c3b),platform=Mac OS X 10.11.3 x86_64)

>>> userBox = browser.find_element_by_id('ctl00_MainContent_txtUsername')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 234, in find_element_by_id
    return self.find_element(by=By.ID, value=id_)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 712, in find_element
    {'using': by, 'value': value})['value']
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 201, in execute
    self.error_handler.check_response(response)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/errorhandler.py", line 194, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"id","selector":"ctl00_MainContent_txtUsername"}
  (Session info: chrome=49.0.2623.75)
  (Driver info: chromedriver=2.20.353124 (035346203162d32c80f1dce587c8154a1efa0c3b),platform=Mac OS X 10.11.3 x86_64)

>>> from selenium import webdriver
>>> from selenium.webdriver.common.keys import Keys
>>> import getpass
>>> 
>>> browser = webdriver.Chrome()
browser.get('https://www.georgiapower.com/')

>>> browser.get('https://www.georgiapower.com/')
>>> 
>>> signInButton = browser.find_element_by_link_text('My Account Login')
>>> signInButton.click()
>>> userBox = browser.find_element_by_id('ctl00_MainContent_txtUsername')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 234, in find_element_by_id
    return self.find_element(by=By.ID, value=id_)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 712, in find_element
    {'using': by, 'value': value})['value']
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 201, in execute
    self.error_handler.check_response(response)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/errorhandler.py", line 194, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"id","selector":"ctl00_MainContent_txtUsername"}
  (Session info: chrome=49.0.2623.75)
  (Driver info: chromedriver=2.20.353124 (035346203162d32c80f1dce587c8154a1efa0c3b),platform=Mac OS X 10.11.3 x86_64)

>>> userBox = browser.find_element_by_css_selector('span.input')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 402, in find_element_by_css_selector
    return self.find_element(by=By.CSS_SELECTOR, value=css_selector)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 712, in find_element
    {'using': by, 'value': value})['value']
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 201, in execute
    self.error_handler.check_response(response)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/errorhandler.py", line 194, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"css selector","selector":"span.input"}
  (Session info: chrome=49.0.2623.75)
  (Driver info: chromedriver=2.20.353124 (035346203162d32c80f1dce587c8154a1efa0c3b),platform=Mac OS X 10.11.3 x86_64)

>>> userBox = browser.find_element_by_css_selector('span.input')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 402, in find_element_by_css_selector
    return self.find_element(by=By.CSS_SELECTOR, value=css_selector)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 712, in find_element
    {'using': by, 'value': value})['value']
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 201, in execute
    self.error_handler.check_response(response)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/errorhandler.py", line 194, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"css selector","selector":"span.input"}
  (Session info: chrome=49.0.2623.75)
  (Driver info: chromedriver=2.20.353124 (035346203162d32c80f1dce587c8154a1efa0c3b),platform=Mac OS X 10.11.3 x86_64)

>>> 
