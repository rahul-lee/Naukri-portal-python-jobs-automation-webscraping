import time
import random
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import os

chrome_browser_path = r'C:\Users\raghu\Downloads\chrome\chrome\chrome.exe'

options = Options()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
# options.add_argument('--headless') 
options.binary_location = chrome_browser_path

chrome_driver_path = r'C:\Users\raghu\OneDrive\Documents\chromedriver\chromedriver\chromedriver.exe'

service = Service(executable_path=chrome_driver_path)

print("Script executed. Fetching jobs...")

# WebDriver with the Service object and the custom Chrome binary
driver = webdriver.Chrome(service=service, options=options)

links = []

for page in range(1, 60):  # number of pages
    url = f"https://www.naukri.com/python-developer-jobs-{page}?k=python+developer"
    driver.get(url)

    time.sleep(random.randrange(2, 5))  # Random delay

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    for job in soup.find_all(attrs={'class': 'cust-job-tuple'}):
        title_link = job.find('a', class_='title', title='Python Developer')
        if title_link:
            link = title_link.get('href')
            if link:
                links.append(link)

print(f"Collected {len(links)} job links")

salary = []
experience = []
location = []
company = []
posted_on = []

for link in links:
    driver.get(link)
    time.sleep(random.randint(2, 5))  # Random delay to simulate human-like behavior
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    try:
        exp_div = soup.find(attrs={'class': 'styles_jhc__exp__k_giM'})
        exp = exp_div.find('span').text.strip() if exp_div else "N/A"
        experience.append(exp)

        post_div = soup.find(attrs={'class': 'styles_jhc__stat__PgY67'})
        posted = post_div.find('span').text.strip() if post_div else "N/A"
        posted_on.append(posted) 

        sal = soup.find(attrs={'class': 'styles_jhc__salary__jdfEC'})
        salary.append(sal.text.strip() if sal else "N/A")

        loc_div = soup.find(attrs={'class': 'styles_jhc__location__W_pVs'})
        location_text = loc_div.find('a').text.strip() if loc_div else "N/A"
        location.append(location_text)

        comp = soup.find(attrs={'class': 'styles_jd-header-comp-name__MvqAI'})
        company_name = comp.find('a').get('title').strip() if comp else "N/A"
        company.append(company_name)


    except Exception as e:
        print(f"Error while processing link {link}: {e}")
        continue

print(f"Lengths - Links: {len(links)}, Experience: {len(experience)}, Salary: {len(salary)}, Location: {len(location)}, Company: {len(company)}")


def generate_unique_filename(base_filename="python_developer_jobs", extension=".xlsx"):
    i = 0
    filename = f"{base_filename}{extension}"
    while os.path.exists(filename):
        i += 1
        filename = f"{base_filename}({i}){extension}"
    return filename

try:
    job_details_df = pd.DataFrame({
        'Company': company,
        'Experience': experience,
        'Salary': salary,
        'Location': location,
        'Posted by': posted_on,
        'Job Link': links
    })
    
    output_filename = generate_unique_filename(base_filename="python_developer_jobs", extension=".xlsx")
    
    job_details_df.to_excel(output_filename, index=False)
    print(f"Job details saved to '{output_filename}'")
except Exception as e:
    print(f"Error saving to Excel: {e}")


driver.quit()
print("Script finished...")
