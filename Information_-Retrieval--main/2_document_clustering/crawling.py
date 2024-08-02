import requests
from bs4 import BeautifulSoup

# Define the URL of the CNN Sports page
url = "https://www.bbc.com/business/future-of-business"

# Send a GET request to fetch the raw HTML content
response = requests.get(url)
if response.status_code != 200:
    print(f"Failed to retrieve page, status code: {response.status_code}")
    exit()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find all elements that contain sports headlines
# Note: Adjust the tag and class name based on the actual HTML structure of the CNN Sports page
headlines = soup.find_all('p')

# Open a text file to write the headlines
with open('sports_headlines.txt', 'w', encoding='utf-8') as file:
    # Iterate through the headlines and write up to 40 of them
    for i, headline in enumerate(headlines):
        if i >= 40:  # Limit to 40 headlines
            break
        file.write(headline.get_text(strip=True) + '\n')

print("Headlines have been saved to sports_headlines.txt")
