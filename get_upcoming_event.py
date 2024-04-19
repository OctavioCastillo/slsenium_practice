# TODO: Extract upcoming event an duse them to fill a dictionary

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)

driver.get("https://www.python.org/")

event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
#for time in event_times:
#    print(time.text)

event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
#for event in event_names:
#    print(event.text)

events = {}

for n in range(len(event_times)):
    events[n+1] = {
        "time": event_times[n].text,
        "name": event_names[n].text
    }

print(events)

driver.quit()