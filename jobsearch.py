from selenium import webdriver
from bs4 import BeautifulSoup
import requests

browser = webdriver.Chrome(executable_path= "d:\chromedriver.exe")

#======================== Open Portal ===============================#
browser.get("https://www.uoftengcareerportal.ca/students/login.htm")

def get_creds():

    id = input("Enter Student ID: \n")
    password = input("Enter password: \n")
    return id,password

# id, password = get_creds()
id, password = '1004476550','arceatom'



#=================== Login Page ========================#
student_id_ID = "j_username"
password_ID = "j_password"
login_button_xpath = '//*[@id="loginForm"]/div[3]/input'


#enter in credential keys#
browser.find_element_by_id(student_id_ID).send_keys(id)
browser.find_element_by_id(password_ID).send_keys(password)

browser.find_element_by_xpath(login_button_xpath).click()

# Click 'Job Postings' button
browser.find_element_by_xpath('//*[@id="mainContentDiv"]/div[2]/div/div[1]/div/a[2]').click();

# Click
browser.find_element_by_xpath('//*[@id="searchPostings"]/div[2]/div/ul/li/a').click();

# Click 'For My Program' button
browser.find_element_by_xpath('//*[@id="dashboard"]/div[2]/div[1]/a').click();


#========================================= filtering jobs===========================#
#list of all job_ids
job_ids = []
stable = 0
while (stable != 1): #iterate through all pages until page does not change
    col_1 = browser.find_elements_by_xpath('//*[@id="postingsTable"]/tbody//td[1]')  #selenium elements
    for id in col_1:
        job_ids.append(id.text)
    #change the page

    return True
