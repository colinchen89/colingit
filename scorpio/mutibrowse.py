import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
lists=['chrome','internet explorer']
for browser in lists :
    driver=webdriver.Remote(
        command_executor="http://127.0.0.1:4444/wd/hub",
        desired_capabilities={'platform':'ANY',
                              'browserName':browser,
                              'version':'',
                              'javascriptEnabled':True

                              })

driver.get("http://www.baidu.com")
driver.find_element_by_id("kw").send_keys("a")
driver.find_element_by_id("su").click()
time.sleep(5)
driver.quit()