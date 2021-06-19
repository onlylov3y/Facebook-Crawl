from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from const import *

browser  = webdriver.Chrome(executable_path=CHROMEDRIVER)

browser.get("http://facebook.com")

txtUser = browser.find_element_by_id("email")
txtUser.send_keys("aldahkconnie@hotmail.com") 

txtPass = browser.find_element_by_id("pass")
txtPass.send_keys("IY43sqolmy161101")

txtPass.send_keys(Keys.ENTER)

sleep(10)

browser.close()