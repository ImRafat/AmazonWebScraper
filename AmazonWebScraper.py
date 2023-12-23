from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import json
import os

search = input("Please input the keyword you want to search for potential products....")

# Create an instance of the Chrome web driver
# Create an instance of the Chrome web driver using webdriver_manager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Navigate to the Amazon homepage
driver.get("https://www.amazon.com")

# Find the search box element using its ID
search_box = driver.find_element(By.ID, "twotabsearchtextbox")

search_box.send_keys(search)

driver.find_element(By.ID, "nav-search-submit-button").click()

item_elements = driver.find_elements(By.CSS_SELECTOR, "s-result-item")

print(item_elements)

for item in item_elements:
    title_element = item.find_element(By.CSS_SELECTOR, "a-size-base-plus")
    print(title_element.text)

data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Convert the dictionary to a JSON object
with open("data.json", "w") as outfile:
    # Write the JSON object to the file
    json.dump(data, outfile)

# Close the browser
#driver.close()
time.sleep(10)