#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 15:00:07 2020

@author: Danya
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from pynput.keyboard import Key, Controller
import random 
option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")


#define typing messages
def type_string_with_delay(string):
    for character in string:  # Loop over each character in the string
        keyboard.type(character)  # Type the character
        delay = random.uniform(0, 0.2)  # Generate a random number between 0 and 10
        time.sleep(delay)  # Sleep for the amount of seconds generated


# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 1 })

driver = webdriver.Chrome(chrome_options=option, executable_path='/Users/Danya/Downloads/chromedriver 2')
driver.get('https://www.facebook.com')


#log into facebook
keyboard = Controller()
username = r'username'
password = r'password'
url = r'https://www.facebook.com/'

driver.find_element_by_id(r'email').send_keys(username)
driver.find_element_by_id(r'pass').send_keys(password)

time.sleep(2)

#driver.find_element_by_id('loginbutton').click()
keyboard.press(Key.enter)
keyboard.release(Key.enter)

time.sleep(3)

#csv

Links = ['link1', 'link2', 'link3'] #insert links to facebook profiles whom you want to send a message to

#for loop to message all the people in Links
for i in Links:
    driver.get(i)
    time.sleep(random.randint(2, 4))
    continue_link = driver.find_element_by_link_text('Message').click()
    time.sleep(random.randint(2, 4))
    type_string_with_delay("Hi, I am just a sample BOT. I was made for fun to see what selenium module can do.") #write your message here
    time.sleep(random.randint(2, 4))
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(random.randint(3, 5))


