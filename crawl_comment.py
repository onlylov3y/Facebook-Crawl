# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from const import *
from selenium.webdriver.chrome.options import Options

option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 1 
})
# Browser init
browser = webdriver.Chrome(chrome_options=option, executable_path=CHROMEDRIVER)
# Fb Login
browser.get("http://facebook.com")
txtUser = browser.find_element_by_id("email")
txtUser.send_keys("aldahkconnie@hotmail.com") 
txtPass = browser.find_element_by_id("pass")
txtPass.send_keys("IY43sqolmy161101")
txtPass.send_keys(Keys.ENTER)
sleep(10)
# open a post
browser.get("https://www.facebook.com/onlylov3y/posts/1722962464519672")
sleep(7)


# # comment turn 1
# showcomment_link = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[2]/div/div/div/div/div/div/div/div/div[2]/div[2]/form/div/div[2]/div[1]/div/div[3]/span[1]/a")
# showcomment_link.click()
# sleep(5)

# # comment turn 2
# showmore_link = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[2]/div/div/div/div/div/div/div/div/div[2]/div[2]/form/div/div[3]/div[1]/div/a")
# showmore_link.click()
# sleep(random.randint(5,10))

# showmore_link.click()
# sleep(5)


# #Get element "Binh luan"
# comment_list = browser.find_elements_by_xpath("//div[@aria-label="Bình luận dưới tên Thu Ha vào 19 tuần trước"]")

# # show  comments
# for comment in comment_list:
#     poster = comment.find_element_by_class_name("_6qw4")
#     content = comment.find_element_by_class_name("_3l3x")
#     print("*", poster.text,":", content.text)

# sleep(5)

like_list = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[1]/div/div[1]/div/div[1]/div/span/div/span[2]/span/span")
like_list.click()

sleep(5)

likes = browser.find_elements_by_class_name("q9uorilb")


for like_element in likes:
    liker = like_element.find_element_by_xpath("//a")
    print(liker.text)
    print(liker.tag_name)
    print(liker.parent)
    print(liker.location)
    print(liker.size)
    print(liker.get_property("href"))
    print(liker.get_attribute("href"))
# Close browser
#browser.close()
