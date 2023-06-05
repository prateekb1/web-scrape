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

# Extract the page source
page_source = driver.page_source

# Parse the page source using BeautifulSoup
soup = BeautifulSoup(page_source, 'html.parser')

# Extract the companies' information
collapsible_divs = soup.find_all('div', class_='company-listing__company company-listing__company--collapsible aos-init aos-animate js-open')

# company_names = []
# for comp_name in companies:
#     company_name = comp_name.find('div', class_='company-listing-card__company-name').text.strip()
#     company_names.append(company_name)
# Create a list to store the extracted data8
company_data = []

# Iterate over each company
for collapsible_div in collapsible_divs:
    # Extract the company name from the collapsible div
    company_name = collapsible_div.find('div', class_='company-listing-card__company-name').text.strip()
    print(company_name)

    # Extract the additional information from inside the collapsible div
    long_description = collapsible_div.find('div', class_='company__long-description').text.strip()
    contacts = collapsible_div.find('div', class_='company__contacts').text.strip()
    categories = collapsible_div.find('div', class_='company__categories').text.strip()
    print(long_description)
    print(contacts)
    print(categories)
    
    # Store the data in a dictionary
    company_info = {
        'Company Name': company_name,
        'Long Description': long_description,
        'Contacts': contacts,
        'Categories': categories
    }
    
    # Append the company info to the list
    company_data.append(company_info)


