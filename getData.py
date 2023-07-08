from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import keyboard


import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_extension('./zip.zip')
emailWithoutDomain = input('Please, enter an email without domain(Mohdabo2023+testDDD=)\n')
domain = input('Please, enter you domain(@gmail.com) \n')
startNumber = input('Please, enter number,from which you want to start \n')
endNumber = input('Please, enter number where you want to end \n')
delay = input('Please, enter your delay \n')
delay = int(delay)
startNumber = int(startNumber)
endNumber = int(endNumber)

driver = webdriver.Chrome(executable_path='./chromedriver.exe',options=chrome_options)
driver.get('https://www.rogers.com/rpp/preferred/request')
print('Did you enter an email in extention?(Enter to confirm)')
keyboard.wait('Enter')

while startNumber <= endNumber:
    driver.get('https://www.rogers.com/rpp/preferred/request')
    time.sleep(delay)
    firstName = driver.find_element(By.XPATH, '//input[@formcontrolname="firstName"]')
    firstName.send_keys("X")
    LastName = driver.find_element(By.XPATH, '//input[@formcontrolname="lastName"]')
    LastName.send_keys("Y")

    phoneNumber = driver.find_element(By.XPATH, '//input[@formcontrolname="phoneNumber"]')
    phoneNumber.click()
    phoneNumber.send_keys('11111111111')

    email = driver.find_element(By.XPATH, '//input[@formcontrolname="email"]')
    email.send_keys(emailWithoutDomain + str(startNumber) + domain)

    phoneNumber = driver.find_element(By.XPATH, '//input[@formcontrolname="postalCode"]')
    phoneNumber.click()
    phoneNumber.send_keys('l8l8l8')

    submit = driver.find_element(By.CLASS_NAME, 'submit-button')
    submit.click()
    time.sleep(delay)
    startNumber += 1

