from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True) # To make sure the window doesn't close automaticly

driver = webdriver.Chrome(options=chrome_options)

driver.get("http://secure-retreat-92358.herokuapp.com/")

f_name = driver.find_element(By.NAME, value="fName")
l_name = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")
button = driver.find_element(By.CLASS_NAME, value="btn")

f_name.send_keys("Octavio")
l_name.send_keys("Castillo")
email.send_keys("octavio@email.com")
button.click()
