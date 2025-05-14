import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest



# Send request
url = "https://wuzzuf.net/saudi/search/jobs/?a=hpb%7Cspbg&q=ml&start=0"
result = requests.get(url)

# Parse content
src = result.content
soup = BeautifulSoup(src, "lxml")

# Extract data
job_titles = soup.find_all("h2", {"class": "css-m604qf"})
company_names = soup.find_all("a", {"class": "css-17s97q8"})
location_names = soup.find_all("span", {"class": "css-5wys0k"})
job_skills = soup.find_all("div", {"class": "css-y4udm8"})

# Prepare lists
job_title = []
company_name = []
location_name = []
job_skill = []
link = []

# Zip through all items safely
for title, company, location  , skill in zip(job_titles,  company_names, location_names, job_skills):
    job_title.append(title.text.strip())
    link.append(title.find("a").attrs["href"])
    company_name.append(company.text.strip().replace("-" , ""))
    location_name.append(location.text.strip())
    job_skill.append(skill.text.strip().replace("·"," | "))


# Export to CSV
file_list = [job_title, company_name, location_name , job_skill,link]
exported = zip_longest(*file_list)

with open(r'E:\labtob\Project paython\Web Scraping\jop.csv', 'w', newline='', encoding='utf-8') as myfile:
    writer = csv.writer(myfile)
    writer.writerow(['Job Title',  'Company Name', 'Location Name' , 'Job Skills','Link'])
    writer.writerows(exported)
