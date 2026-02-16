# import undetected_chromedriver as uc
# driver = uc.Chrome(headless=True,use_subprocess=False)

# from selenium.webdriver import Chrome

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# import json

# driver = Chrome()
# driver.get( 'https://www.amazon.com/s?k=laptop&crid=7RVWXM42GIWG&sprefix=laptop%2Caps%2C328&ref=nb_sb_noss_1' )

# headline_element = driver.find_element(By.CSS_SELECTOR, "[data-cy=\"headline\"]")

# title_element = headline_element.find_element(By.CSS_SELECTOR, "h1")
# title = title_element.text

# tagline_element = headline_element.find_element(By.CSS_SELECTOR, "h2")
# tagline = tagline_element.text

# description_element = headline_element.find_element(By.CSS_SELECTOR, "[data-cy=\"description\"]")
# description = description_element.text
# product = {
#   "title": title,
#   "tagline": tagline,
#   "description": description
# }

# with open("product.json", "w") as json_file:
#   json.dump(product, json_file, indent=4)
  
# # Close the browser and release its resources
# driver.quit()


import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import json
import time

from selenium import webdriver

# Create a Chrome web driver instance
driver = webdriver.Chrome()
time.sleep(5)

# Connect to the target page
driver.get("https://www.amazon.com/s?k=laptop&crid=7RVWXM42GIWG&sprefix=laptop%2Caps%2C328&ref=nb_sb_noss_1")

time.sleep(5)
# Scraping logic
headline_element = driver.find_element(By.XPATH, "(//div/a/h2/span){i}").text

title_element = headline_element.find_element(By.CSS_SELECTOR, "h1")
title = title_element.text

tagline_element = headline_element.find_element(By.CSS_SELECTOR, "h2")
tagline = tagline_element.text

description_element = headline_element.find_element(By.CSS_SELECTOR, "[data-cy=\"description\"]")
description = description_element.text

# Populate a dictionary with the scraped data
product = {
  "title": title,
  "tagline": tagline,
  "description": description
}

# Export the scraped data to JSON
with open("product.json", "w") as json_file:
  json.dump(product, json_file, indent=4)

# Close the browser and release its resources
driver.quit() 


