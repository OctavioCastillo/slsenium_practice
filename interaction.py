from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys # Press different keys in keyboard

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")

# click the anchor tag
#count.click()

# Find element by link text
#all_portals = driver.find_element(By.LINK_TEXT, value="Most viewed pages")
#all_portals.click()

# Write 
search = driver.find_element(By.NAME, value="search")

# Send keys
search.send_keys("Python", Keys.ENTER)


