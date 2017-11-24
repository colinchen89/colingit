import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
driver=webdriver.Remote(
    command_executor="http://192.168.50.78:4444/wd/hub",
    desired_capabilities=DesiredCapabilities.CHROME)

driver.get("http://www.baidu.com")
driver.find_element_by_id("kw").send_keys("a")
driver.find_element_by_id("su").click()
time.sleep(5)
driver.quit()