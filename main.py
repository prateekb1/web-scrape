import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

# Specify the URL
urlpage = 'https://www.sequoiacap.com/india/our-companies/'

# Run Firefox webdriver from the executable path of your choice
driver = webdriver.Firefox()

# Get web page
driver.get(urlpage)

# Wait for the cookie notice to appear
wait = WebDriverWait(driver, 10)
cookie_notice = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'cookie-notice__message')))

# Close the cookie notice if it is displayed
if cookie_notice.is_displayed():
    close_button = driver.find_element(By.CLASS_NAME, 'js-cookie-accept')
    close_button.click()

# Execute script to scroll down the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Wait for 2 seconds for the page to load
time.sleep(2)

# Find the "Load More" button element
load_more_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Load More')]")

# Click the "Load More" button until it is no longer visible
# while load_more_button.is_displayed():
#     driver.execute_script("arguments[0].scrollIntoView();", load_more_button)
#     load_more_button.click()
#     time.sleep(2)
#     load_more_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Load More')]")

# Extract the page source
page_source = driver.page_source

# Parse the page source using BeautifulSoup
soup = BeautifulSoup(page_source, 'html.parser')

# Extract the companies' information
companies = soup.find_all('div', class_='company-listing-card company-listing-card--collapsible')

company_names = []
for comp_name in companies:
    company_name = comp_name.find('div', class_='company-listing-card__company-name').text.strip()
    company_names.append(company_name)

# Create a list to store the extracted data8
company_data = []

element = driver.find_element(By.XPATH, f"//*[contains(text(), '90 seconds')]")
# Click on the company-listing-card__indicator to open the details box
element.click()
time.sleep(2)  # Wait for the details box to open

# Extract the required information from the details box
# company_name = driver.find_element(By.CLASS_NAME, 'company-listing-card__company-name').text.strip()

long_description = driver.find_element(By.CLASS_NAME, 'company__long-description').text.strip()
contacts = driver.find_element(By.CLASS_NAME, 'company__contacts').text.strip()
categories = driver.find_element(By.CLASS_NAME, 'company__categories').text.strip()
print(company_names[2])
print(long_description)
print(contacts)
print(categories)

# Iterate over each company
# for company in company_names:
#     # Find the company element again
#     element = driver.find_element(By.XPATH, f"//*[contains(text(), '{company}')]")
#     # Click on the company-listing-card__indicator to open the details box
#     element.click()
#     time.sleep(2)  # Wait for the details box to open
    
#     # Extract the required information from the details box
#     # company_name = driver.find_element(By.CLASS_NAME, 'company-listing-card__company-name').text.strip()

#     long_description = driver.find_element(By.CLASS_NAME, 'company__long-description').text.strip()
#     contacts = driver.find_element(By.CLASS_NAME, 'company__contacts').text.strip()
#     categories = driver.find_element(By.CLASS_NAME, 'company__categories').text.strip()
#     print(company)
#     print(long_description)
#     print(contacts)
#     print(categories)
    
#     # Store the data in a dictionary
#     company_info = {
#         'Company Name': company,
#         'Long Description': long_description,
#         'Contacts': contacts,
#         'Categories': categories
#     }
    
#     # Append the company info to the list
#     company_data.append(company_info)
    
#     # Close the details box by clicking on the indicator again
#     element.click()
#     time.sleep(1)  # Wait for the details box to close

# Close the webdriver
driver.quit()

# Create a DataFrame from the extracted data
df = pd.DataFrame(company_data)

# Save the DataFrame to a CSV file
df.to_csv('company_data.csv', index=False)
