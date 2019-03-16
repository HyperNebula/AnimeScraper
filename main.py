import requests
from bs4 import BeautifulSoup

url = "https://myanimelist.net/anime.php?q=samuri%20champloo"

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

result = soup.find(class_='hoverinfo_trigger fw-b fl-l')
result_link = result['href']

# new page
url = result_link

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

name = soup.find("span", itemprop="name").text
image_url = soup.find("img", itemprop="image")['src']
description = soup.find("span", itemprop="description").text
score = soup.find("span", itemprop="ratingValue").text
# episode_num = soup.find("span", id="curEps").text

raw_info = soup.find("div", class_="js-scrollfix-bottom")
for item in raw_info:
    if "Rating:" in str(item):
        rating = item.text.replace("Rating:\n", "").strip()
    elif "English:" in str(item):
        eng_name = item.text.replace("English: ", "").strip()
    elif "Duration:" in str(item):
        duration = item.text.replace("Duration:\n", "").strip()
    elif "Genres:" in str(item):
        genres = item.text.replace("Genres:\n", "").strip()
    elif "Status:" in str(item):
        status = item.text.replace("Status:\n", "").strip()
    elif "Episodes:" in str(item):
        episode_num = item.text.replace("Episodes:\n", "").strip()
    elif "Premiered:" in str(item):
        premiere_date = item.text.replace("Premiered:\n", "").strip()

