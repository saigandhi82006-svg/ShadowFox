import requests
from bs4 import BeautifulSoup
import csv

# Step 1: Website URL
url = "https://quotes.toscrape.com"

# Step 2: Send request to website
response = requests.get(url)

# Step 3: Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Step 4: Find required data
quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")

# Step 5: Save data to CSV
with open("quotes.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Quote", "Author"])

    for i in range(len(quotes)):
        writer.writerow([quotes[i].text, authors[i].text])

print("✅ Data scraped and saved successfully!")
