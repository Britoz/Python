from selenium import webdriver
# TODO: allowing the web driver to perform more complex tasks like drag and dropping
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome('../chromedriver_win32/chromedriver.exe')

driver.maximize_window()
driver.get('http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')


source = driver.find_element_by_xpath('//*[@id="box3"]')
dest = driver.find_element_by_xpath('//*[@id="box103"]')

actions = ActionChains(driver)

# TODO: source is destination
actions.drag_and_drop(source, dest).perform()