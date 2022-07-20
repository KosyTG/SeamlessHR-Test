
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver_service = Service(executable_path="/Users/apple/Downloads/chromedriver")

driver = webdriver.Chrome(service=driver_service)

driver.get('https://the-internet.herokuapp.com/')

form_authentication = driver.find_element(By.CSS_SELECTOR,"#content > ul > li:nth-child(21) > a").click()

#LOGIN
driver.find_element(By.CSS_SELECTOR,"#username").send_keys("tomsmith");
driver.find_element(By.CSS_SELECTOR,"#password").send_keys("SuperSecretPassword!");
driver.find_element(By.CSS_SELECTOR,"#login > button > i").click()

#VALIDATE VALID LOGIN
valid_login = driver.find_element(By.CSS_SELECTOR, "#flash")
print(valid_login.is_displayed())
print("You logged into a secure area!")