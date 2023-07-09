from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import keyboard

def BtnClickAhead():
    wait = WebDriverWait(driver, 15)  
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'submit-button')))
    submit = driver.find_element(By.CLASS_NAME, 'submit-button')
    submit.click()
    wait = WebDriverWait(driver, 15)  
    wait.until(EC.presence_of_element_located((By.XPATH, '//button[@title="Continue with verification process"]')))
    btn = driver.find_element(By.XPATH, '//button[@title="Continue with verification process"]')
    btn.click()
def BtnClickBack():
    wait = WebDriverWait(driver, 15)  
    wait.until(EC.presence_of_element_located((By.XPATH, '//button[@title="common.backHint"]')))
    btnBack1 = driver.find_element(By.XPATH, '//button[@title="common.backHint"]')
    btnBack1.click()
    wait = WebDriverWait(driver, 15)  
    wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="Back"]')))
    btnBack2 = driver.find_element(By.XPATH, '//span[text()="Back"]') 
    btnBack2.click()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_extension('./zip.zip')
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 15.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36")

emailWithoutDomain = input('Please, enter an email without domain(Mohdabo2023+testDDD=)\n')
domain = input('Please, enter you domain(@gmail.com) \n')
startNumber = input('Please, enter number,from which you want to start \n')
endNumber = input('Please, enter number where you want to end \n')
startNumber = int(startNumber)
endNumber = int(endNumber)

driver = webdriver.Chrome(executable_path='./chromedriver.exe',options=chrome_options)
driver.get('https://www.rogers.com/rpp/preferred/request')

print('Did you enter an email in extention?(Enter to confirm)')
keyboard.wait('Enter')

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

startNumber += 1
BtnClickAhead()
BtnClickBack()

while startNumber <= endNumber:
    wait = WebDriverWait(driver, 15)  
    wait.until(EC.presence_of_element_located((By.XPATH, '//input[@formcontrolname="email"]')))
    email = driver.find_element(By.XPATH, '//input[@formcontrolname="email"]')
    email.send_keys(Keys.BACKSPACE * len(email.get_attribute('value')))
    email.send_keys(emailWithoutDomain + str(startNumber) + domain)
    BtnClickAhead()
    BtnClickBack()
    startNumber += 1
driver.quit()
driver.close()
