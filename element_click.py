from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Specify the name you want to find and click on
name_to_find = "99.co"

# Instantiate the webdriver (choose the appropriate driver for your browser)
driver = webdriver.Firefox()

# Open the website
driver.get("https://www.sequoiacap.com/india/our-companies/")  # Replace with the actual website URL

# Find the element with the specified name
element = driver.find_element(By.XPATH, f"//*[contains(text(), '{name_to_find}')]")

# Click on the element
element.click()
time.sleep(10)

# Close the webdriver
driver.quit()
