import datetime
from datetime import datetime
import pandas as pd
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import json
import time

from selenium import webdriver

# Create a Chrome web driver instance
driver = webdriver.Chrome()
time.sleep(5)
driver.maximize_window()
processed_data = []

# Connect to the target page
for i in range(1,20):
  driver.get(f"https://www.amazon.com/s?k=electronic+tablets&page={i}&xpid=Kb09TIwp2AP1K&_encoding=UTF8&content-id=amzn1.sym.f0670b1b-e1fd-4c67-a2b1-b8a347243628&pd_rd_r=357b0bfd-1927-4dd1-953e-357d95f05740&pd_rd_w=rq7jY&pd_rd_wg=DujFk&qid=1771324497&ref=sr_pg_2")

  time.sleep(5)
  # Scraping logic
  products = driver.find_elements(By.XPATH, "//div[@class='a-section']/div")
  for product in products:
      try:
          title = product.find_element(By.XPATH, ".//h2/span").text
          print(title)
      except:
          title = "N/A"
        
      try:
          rating = product.find_element(By.XPATH, "(.//span[@class='a-size-small a-color-base'])").text
          print(rating)
      except:
          rating = "N/A"
        
      try:
          total_rating = product.find_element(By.XPATH, "(.//span[@class='a-size-mini puis-normal-weight-text s-underline-text'])").text
          print(total_rating)
      except:
          total_rating = "N/A"
        
      try:
          price = product.find_element(By.XPATH, "(.//span[@class='a-price-whole'])").text
          print(price)
      except:
          price = "N/A"


  # Populate a dictionary with the scraped data
      product = {
        "title": title,
        "rating": rating,
        "total_rating":total_rating,
        "price": price
      }
      processed_data.append(product)

  # # Export the scraped data to JSON
  with open("products.json", "w") as json_file:
    json.dump(processed_data, json_file, indent=4)
    
  # Convert processed data to a Pandas DataFrame
  df = pd.DataFrame(processed_data)

    # Export DataFrame to CSV with current_datetime format
  current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M")
  csv_filename = f'products_{current_datetime}.csv'
  df.to_csv(csv_filename, index=False, encoding='utf-8')

# Close the browser and release its resources
driver.quit() 





