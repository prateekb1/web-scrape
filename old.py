import csv
import requests
from bs4 import BeautifulSoup

# Send a GET request to the website
url = 'https://www.sequoiacap.com/india/our-companies/'
response = requests.get(url)

# Create a BeautifulSoup object
soup = BeautifulSoup(response.text, 'html.parser')



# Find the div elements containing the data based on the class names
class_names = [
    'company-listing-card__header',
    'company-listing-card__company-description',
    'company__contacts',
    'company__categories'
]

data = []
for i in range(len(class_names)):
    elements = soup.find_all('div', class_=class_names[i])
    print(elements)
    for j in range(len(elements)):
        if class_names[i] == 'company__contacts':
            div_element = soup.find('div', class_='company__contacts')
            a_element = div_element.find('a').get_text(strip=True)
            data[j].append(a_element)
            print(a_element)
        elif class_names[i] == 'company__categories':
            span_elements = elements[j].find_all('span', class_='pill')
            categories = [span.get_text(strip=True) for span in span_elements]
            data[j].extend(categories)
        else:
            if len(data) <= j:
                data.append([elements[j].get_text(strip=True)])
            else:
                data[j].append(elements[j].get_text(strip=True))

# Save the data to a CSV file
csv_filename = 'sequoia_data.csv'
with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(class_names)
    writer.writerows(data)
print(f"Data has been fetched and saved to {csv_filename} successfully.")

# Read the CSV file
with open(csv_filename, 'r', newline='', encoding='utf-8') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)
