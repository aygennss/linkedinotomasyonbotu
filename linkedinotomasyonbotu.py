# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 23:34:55 2023

@author: AYGENN
"""

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

browser=webdriver.Chrome("C:/Users/AYGENN/OneDrive/Masaüstü/chromedriver.exe")
browser.get("https://tr.linkedin.com/")
browser.fullscreen_window()
time.sleep(2)

login=browser.find_element("xpath", "/html/body/nav/div/a[2]")
login.click()
time.sleep(3)
email=browser.find_element("xpath", "//*[@id='username']")
sifre=browser.find_element("xpath", "//*[@id='password']")

email.send_keys("mail@gmail.com")
sifre.send_keys("sifre.")

login.button=browser.find_element("xpath", "//*[@id='organic-div']/form/div[3]/button")
login.button.click()
time.sleep(5)
search_bar=browser.find_element("xpath", "//*[@id='global-nav-typeahead']/input")
search_bar.send_keys("#python")
search_bar.send_keys(Keys.RETURN)
time.sleep(10)

contacts=browser.find_element("xpath", "//*[@id='global-nav']/div/nav/ul/li[2]/a/span")
contacts.click()

time.sleep(5)

contacts_button=browser.find_element("xpath","//*[@id='ember388']/div/div[1]")
contacts_button.click()
time.sleep(15)

for i in range(1,3):
    browser.execute_script("window.scrollTo(0, document.body.scrolHeight)")
    time.sleep(3)
    
followers=browser.find_elements("xpath","//*[@id='ember690']/div[2]/div[1]/ul/li[2]/div/div/div[1]")

followeList=[]
for follower in followers:
     
    followeList.append(follower.text)
with open ("follower.txt","w", encoding=("UTF-8")) as file:
    for follower in followeList:
        file.write(follower +"/n")
time.sleep(5)
     



browser.quit()
