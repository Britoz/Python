from selenium import webdriver

# initualize web driver for chrome
driver = webdriver.Chrome('../chromedriver_win32/chromedriver.exe')
'''
need specific link to chromedriver.exe because of the unmatch PATH with python
'''
driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

messageField = driver.find_element_by_xpath('//*[@id="user-message"]')

messageField.send_keys('Hello world')
showMessageButton = driver.find_element_by_xpath('//*[@id="get-input"]/button')
showMessageButton.click()

additionField1 = driver.find_element_by_xpath('//*[@id="sum1"]')
additionField1.send_keys('Nhu Heo')
additionField2 = driver.find_element_by_xpath('//*[@id="sum2"]')
additionField2.send_keys('tnq')

GettotalClickButton = driver.find_element_by_xpath('//*[@id="gettotal"]/button')
GettotalClickButton.click()