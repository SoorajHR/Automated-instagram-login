#pip install selenium if you don't have it installed
from selenium import webdriver
from time import sleep

#declaring a variable

username = input("Enter User name/email = ")
password = input("Enter password = ")

driver = webdriver.Chrome()
# Navigate to the login page of your web application
driver.get("https://www.instagram.com/")
#allow some time for the page to load before moving on
sleep(2)
#look for the username field
USERNAME = driver.find_element("xpath", '//*[@id="loginForm"]/div/div[1]/div/label/input')
#look for the password field
PASSWORD = driver.find_element("xpath", '//*[@id="loginForm"]/div/div[2]/div/label/input')

#USERNAME send key to or assign to variable username
USERNAME.send_keys(username)
# PASSWORD send key to or assign to variable password
PASSWORD.send_keys(password)

sleep(2)
#click on submit button
snd=driver.find_element("xpath", '//*[@id="loginForm"]/div/div[3]').click()
sleep(2)







