from selenium import webdriver
from selenium.webdriver.common.by import By


# Keep Chrome browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
#driver.get("https://www.amazon.com/-/es/Auriculares-cancelaci%C3%B3n-viscoel%C3%A1stica-auriculares-port%C3%A1tiles/dp/B08FX35S7K/ref=sr_1_3?_encoding=UTF8&content-id=amzn1.sym.8148f1e1-83ed-498f-85be-ff288b197da7&dib=eyJ2IjoiMSJ9.FuJ3KWvTPovvHzq-ZOcwdL2qAjo8x-bX4ZCFGzJ6YwVGSQ7uGqsOGO-VeTYlzz95IWgsxWQTL3b003OjDsMYNmuTVAR79PyZ3iYUxkdp34uI-mVej6F-ktguhl8vIJHaT8Z8ymh0Vxic6Ii5yhjAvEq6taEM_1uoWomeQoX_3Bn3ZOEcrGULMc0Xwi68tF55gp5mTP64RSOQ0DAjMQEj-xm1FSDV-mHckFQkw2b-aUw.uZ3Vpq_D9tEaT0jrbV-84OdggoEJtSHoDOnr-sXlZfY&dib_tag=se&keywords=gaming+headsets&pd_rd_r=1c0a6c1e-d330-49ff-9c9e-1df563b47470&pd_rd_w=YB3nF&pd_rd_wg=yZVaN&pf_rd_p=8148f1e1-83ed-498f-85be-ff288b197da7&pf_rd_r=2CGNJ72JG1C6K04P7JS6&qid=1713312784&sr=8-3")

#price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
#price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
#print(f"The price is {price_dollar.text}.{price_cents.text}")

driver.get("https://www.python.org/")
search_bar = driver.find_element(By.NAME, value="q")
print(search_bar.get_attribute("placeholder"))

button = driver.find_element(By.ID, value="submit")
print(button.size)

documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print(documentation_link.text)

# search by xpath
bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)

#driver.close() # close particular tab
driver.quit() #close all the tabs

