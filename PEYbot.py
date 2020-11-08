# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 13:19:23 2020

@authors: Spencer Ball, Atom Arce, Shyam Menon
"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import questionary 


# User enters PEY portal credentials
portal_ID = questionary.text("Enter PEY portal ID (username)").ask()
portal_pass = questionary.password("Enter PEY portal password").ask()



# ========== User customizable job search criteria ==========

# Discipline selection
disciplines = questionary.checkbox(
          'Select desired disciplines',
          choices=[
              "Actuarial",
              "Chemical Engineering",
              "Civil Engineering",
              "Engineering Science (Aerospace)",
              "Engineering Science (Machine Intelligence)",
              "Engineering Science (Electrical and Computer)",
              "Math & Stats"
             ]).ask()

# Key words 
keywords = []
again = True
while again == True:
   word = questionary.text("Enter a word you would like included in job description (enter -1 to continue)").ask()
   
   if word == '-1':
      again = False
      break
   
   keywords.append(word)


# ========== Navigating to the 'Search Job Postings' section ==========

# Initiate the browser
browser = webdriver.Chrome(ChromeDriverManager().install())

# Open the Website
browser.get('https://www.uoftengcareerportal.ca/students/login.htm')

# Fill credentials
browser.find_element_by_name('j_username').send_keys(portal_ID)
browser.find_element_by_name('j_password').send_keys(portal_pass)

# Click 'Log In' button
browser.find_element_by_xpath('//*[@id="loginForm"]/div[3]/input').click();

# Click 'Search Postings' button
browser.find_element_by_xpath('//*[@id="mainContentDiv"]/div[2]/div/div[1]/div/a[2]').click();

# Click 'Co-Op & Experience Positings'
browser.find_element_by_xpath('//*[@id="searchPostings"]/div[2]/div/ul/li/a').click();

# Click 'Search Job Postings'
browser.find_element_by_xpath('//*[@id="mainContentDiv"]/div[2]/div/div/div/a[2]').click();


# ========== Job Search Filtering process ==========

job_desc_box = browser.find_element_by_xpath('//*[@id="JobDescription_op"]/option[2]')       

browser.execute_script("arguments[0].scrollIntoView();", job_desc_box)    # scroll until desired item is in view
job_desc_box.click();

for word in keywords:
   browser.find_element_by_name('JobDescription').send_keys(word,' ')


# Dictionary for storing (discipline: xpath) pairs
disci_dict = {'Actuarial': '//*[@id="postingForm"]/div/div[2]/div/div/div[14]/div[2]/select/option[2]', 
              'Chemical Engineering': '//*[@id="postingForm"]/div/div[2]/div/div/div[14]/div[2]/select/option[3]', 
              'Civil Engineering': '//*[@id="postingForm"]/div/div[2]/div/div/div[14]/div[2]/select/option[4]', 
              'Engineering Science (Aerospace)': '//*[@id="postingForm"]/div/div[2]/div/div/div[14]/div[2]/select/option[9]',
              'Engineering Science (Machine Intelligence)': '//*[@id="postingForm"]/div/div[2]/div/div/div[14]/div[2]/select/option[14]',
              'Engineering Science (Electrical and Computer)': '//*[@id="postingForm"]/div/div[2]/div/div/div[14]/div[2]/select/option[11]', 
              'Math & Stats': '//*[@id="postingForm"]/div/div[2]/div/div/div[14]/div[2]/select/option[21]'
              } 

action = ActionChains(browser)
action.key_down(Keys.CONTROL).perform()   # holding ctrl key to select multiple items


for item in disciplines:
   
   where = disci_dict[item]            # getting xpath from each item
   
   element = browser.find_element_by_xpath(where)              
   browser.execute_script("arguments[0].scrollIntoView();", element)    # scroll until desired item is in view
   element.click();
      
      
action.key_up(Keys.CONTROL).perform()     # letting go of ctrl key

      
# Clicking 'Search Job Postings' button to complete the search
element = browser.find_element_by_xpath('//*[@id="postingForm"]/div/div[4]/div/a')
browser.execute_script("arguments[0].scrollIntoView();", element)
element.click();

