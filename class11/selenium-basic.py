from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:/webdriver/chromedriver.exe")

url = "http://github.com"
driver.get(url)

time.sleep(2)
driver.maximize_window()
driver.save_screenshot("github.com-homepage.png")

url = "http://github.com/kartalali"
driver.get(url)

print(driver.title)

if "kartalali" in driver.title:
    driver.save_screenshot("github-alikartal.png")

time.sleep(2)

driver.back()
# driver.forward()

time.sleep(2)

driver.close()