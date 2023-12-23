from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import json

search = input("Please seperate each keyword you want to search with a comma: ")

# Create an instance of the Chrome web driver
# Create an instance of the Chrome web driver using webdriver_manager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#converts it into a list
keyWords = search.split(',');

# Navigate to the Amazon homepage
driver.get("https://www.amazon.com")

for eachItem in keyWords:
    search_box = driver.find_element(By.ID, "twotabsearchtextbox")

    search_box.clear()
    search_box.send_keys(eachItem)

    driver.find_element(By.ID, "nav-search-submit-button").click()

    item_elements = driver.find_elements(By.CLASS_NAME, "s-result-item")

    print(item_elements[1].text)

    for item in item_elements:
        title_element = item.find_element(By.CSS_SELECTOR, "a-size-base-plus")
        print(title_element.text)

    data = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }

    time.sleep(10)
    # Convert the dictionary to a JSON object
    with open("data.json", "w") as outfile:
        # Write the JSON object to the file
        json.dump(data, outfile)
    
# Close the browser
#driver.close()

