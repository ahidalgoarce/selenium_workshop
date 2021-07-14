#import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "D:\DEV\drivers\chromedriver.exe"
browser = webdriver.Chrome(PATH)

browser.get("https://www.google.com")
browser.maximize_window()
search_input = browser.find_element_by_name('q')
search_input.send_keys('hello world')
search_input.send_keys(Keys.RETURN)

time.sleep(3)
browser.quit()