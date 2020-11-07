# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 13:19:23 2020

@author: Spencer
"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


# Initiate the browser
browser  = webdriver.Chrome(ChromeDriverManager().install())

# Open the Website
browser.get('https://www.uoftengcareerportal.ca/students/login.htm')

# Your PEY portal credentials
portal_ID = "1004762599"
portal_pass = "ballspen"

# Fill credentials
browser.find_element_by_name('j_username').send_keys(portal_ID)
browser.find_element_by_name('j_password').send_keys(portal_pass)

# Click 'Log In' button
browser.find_element_by_xpath('//*[@id="loginForm"]/div[3]/input').click();

# Click 'Job Postings' button
browser.find_element_by_xpath('//*[@id="mainContentDiv"]/div[2]/div/div[1]/div/a[2]').click();

# Click
browser.find_element_by_xpath('//*[@id="searchPostings"]/div[2]/div/ul/li/a').click();

# Click 'For My Program' button
browser.find_element_by_xpath('//*[@id="dashboard"]/div[2]/div[1]/a').click();

