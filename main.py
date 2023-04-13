import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="/chromedriver")

driver.get("http://pypi.python.org/pypi/selenium")
driver.save_screenshot('screenshot.png')
time.sleep(10)