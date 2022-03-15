from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:/webdriver/chromedriver.exe")

url = "https://www.google.com"

driver.get(url)