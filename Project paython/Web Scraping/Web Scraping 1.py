import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

# --------------------------------------------------
# Initialize global lists to store scraped data
# --------------------------------------------------
job_title = []
company_name = []
location_name = []
job_skill = []
links = []

# --------------------------------------------------
# Start scraping from the first page
# --------------------------------------------------
page_number = 0

while True:
    print(f"🔎 Fetching page {page_number + 1}...")

    # Send GET request to the Wuzzuf search results page
    url = f"https://wuzzuf.net/saudi/search/jobs/?a=hpb%7Cspbg&q=ml&start={page_number}"
    result = requests.get(url)

    # Parse the HTML content
    src = result.content
    soup = BeautifulSoup(src, "lxml")

    # --------------------------------------------------
    # Check if there are job postings on the page
    # If not, break the loop
    # --------------------------------------------------
    job_titles = soup.find_all("h2", {"class": "css-m604qf"})
    if not job_titles:
        print("🚫 No more jobs found. Stopping...")
        break

    # Extract other job-related information
    company_names  = soup.find_all("a",   {"class": "css-17s97q8"})
    location_names = soup.find_all("span", {"class": "css-5wys0k"})
    job_skills     = soup.find_all("div", {"class": "css-y4udm8"})

    # --------------------------------------------------
    # Iterate over all job listings and extract data
    # --------------------------------------------------
    for title, company, location, skill in zip(job_titles, company_names, location_names, job_skills):
        # Job title
        job_title.append(title.text.strip())

        # Full job link
        link = title.find("a").attrs["href"]
        full_link = link if link.startswith("http") else "https://wuzzuf.net" + link
        links.append(full_link)

        # Company name (cleaned)
        company_name.append(company.text.strip().replace("-", ""))

        # Job location
        location_name.append(location.text.strip())

        # Job skills (formatted)
        job_skill.append(skill.text.strip().replace("·", " | "))

    # Move to the next page
    page_number += 1

# --------------------------------------------------
# Export the collected data to a CSV file
# --------------------------------------------------
file_list = [job_title, company_name, location_name, job_skill, links]
exported = zip_longest(*file_list)

with open(r'E:\labtob\Project paython\Web Scraping\jop.csv', 'w', newline='', encoding='utf-8') as myfile:
    writer = csv.writer(myfile)
    writer.writerow(['Job Title', 'Company Name', 'Location Name', 'Job Skills', 'Link'])
    writer.writerows(exported)

print("✅ Data exported successfully to CSV.")
