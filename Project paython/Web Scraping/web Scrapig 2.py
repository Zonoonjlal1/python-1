# ------------------------------
# Required Libraries
# ------------------------------
import requests
from bs4 import BeautifulSoup
import openpyxl

# ------------------------------
# Load Web Page (Change date as needed)
# ------------------------------
url = 'https://www.yallakora.com/match-center/%D9%85%D8%B1%D9%83%D8%B2-%D8%A7%D9%84%D9%85%D8%A8%D8%A7%D8%B1%D9%8A%D8%A7%D8%AA?date=5/19/2025#days'
page = requests.get(url)

# ------------------------------
# Main Function
# ------------------------------
def main(page):
    # Parse page content using BeautifulSoup
    soup = BeautifulSoup(page.content, "lxml")

    # Initialize list to hold all matches data
    match_details = []

    # Get all championship blocks (each containing multiple matches)
    championships = soup.find_all("div", {"class": "matchCard"})

    # ------------------------------------------
    # Extract match information from a championship
    # ------------------------------------------
    def get_match_info(championship):
        # Extract the name of the championship (e.g., الدوري المصري)
        championship_title = championship.contents[1].find("h2").text.strip()

        # Get all finished matches under this championship
        all_matches = championship.contents[3].find_all("div", {"class": "item finish liItem"})

        # Loop through each match and extract required details
        for match in all_matches:
            # Get team names
            team1 = match.find("div", {"class": "teams teamA"}).text.strip()
            team2 = match.find("div", {"class": "teams teamB"}).text.strip()

            # Get match score (e.g., 2 - 1)
            result_spans = match.find("div", {"class": "MResult"}).find_all("span", {"class": "score"})
            score = f"{result_spans[0].text.strip()} - {result_spans[1].text.strip()}"

            # Get match time (e.g., 9:00 PM)
            time = match.find("div", {"class": "MResult"}).find("span", {"class": "time"}).text.strip()

            # Store match information in dictionary format
            match_details.append({
                "البطولة": championship_title,
                "الفريق الأول": team1,
                "الفريق الثاني": team2,
                "النتيجة": score,
                "توقيت المباراة": time
            })

    # ------------------------------------------
    # Process all championships
    # ------------------------------------------
    for champ in championships:
        get_match_info(champ)

    # ------------------------------
    # Create Excel Workbook and Sheet
    # ------------------------------
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "المباريات"

    # Define Arabic column headers
    headers = ["البطولة", "الفريق الأول", "الفريق الثاني", "النتيجة", "توقيت المباراة"]
    sheet.append(headers)

    # Add match data to the sheet row by row
    for match in match_details:
        sheet.append([
            match["البطولة"],
            match["الفريق الأول"],
            match["الفريق الثاني"],
            match["النتيجة"],
            match["توقيت المباراة"]
        ])

    # ------------------------------
    # Save Excel File
    # ------------------------------
    workbook.save(r"E:\labtob\Project paython\Web Scraping\yallakora_بالعربية.xlsx")
    print("✅ تم حفظ البيانات في الملف بنجاح باللغة العربية.")

# Run the script
main(page)
