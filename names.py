from selenium import webdriver

browser = webdriver.Chrome(executable_path= "C:\chromedriver.exe")

#======================== Open Portal ===============================#
browser.get("https://www.uoftengcareerportal.ca/students/login.htm")

def get_creds():

    id = input("Enter Student ID: \n")
    password = input("Enter password: \n")
    return id,password

# id, password = get_creds()
id, password = '1005057484','menonshy'



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
element = browser.find_element_by_xpath('//*[@id="dashboard"]/div[2]/div[1]/a')
browser.execute_script("arguments[0].scrollIntoView();", element)
element.click();


######################################### Company & Job Names ##############################################

#Xpath should change based on the job posting here
element = browser.find_element_by_xpath('//*[@id="posting27515"]/td[2]/a[1]')
browser.execute_script("arguments[0].scrollIntoView();", element)
element.click();

job_name = browser.find_element_by_xpath('//*[@id="mainContentDiv"]/div[1]/div/div[2]/h1').text
company_name = browser.find_element_by_xpath('//*[@id="postingDiv"]/table[3]/tbody/tr[1]/td[2]').text

#print(job_name)
#print(company_name)