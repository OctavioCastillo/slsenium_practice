from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, value="cookie")

# get items in store
items = driver.find_elements(By.CSS_SELECTOR, value="#store div")
item_ids = [item.get_attribute("id") for item in items]


timeout = time.time() + 3
five_minutes = time.time() + 60*5

while True:
    # Infinite click
    cookie.click()

    # Check eevery 5 seconds
    if time.time() > timeout:

        all_prices = driver.find_elements(By.CSS_SELECTOR, value="#store b")
        item_prices = []

        for price in all_prices:
            element_price = price.text
            if element_price != "":
                cost = int(element_price.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        money = driver.find_element(By.ID, value="money").text # str element
        if "," in money:
            money = money.replace(",", "")
            money = int(money)

        affordable_items = {}
        for cost, id in cookie_upgrades.items():
            if int(money) > cost:
                affordable_items[cost] = id
    
        # Purchase the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_items, default=0)
        print(highest_price_affordable_upgrade)
        if highest_price_affordable_upgrade == 0:
            pass
        else:
            to_purchase_id = affordable_items[highest_price_affordable_upgrade]
            driver.find_element(By.ID, value=to_purchase_id).click()
        
        timeout = time.time() +3

    # Check if the time ends
    if time.time() > five_minutes:
        cookie_per_sec = driver.find_element(By.ID, value="cps").text
        print(cookie_per_sec)
        driver.quit()
        break
    