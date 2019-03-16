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
score = soup.find("div", class_="fl-l score").text.strip()
episode_num = soup.find("span", id="curEps").text

raw_info = soup.find_all("div", class_="spaceit_pad")
name_info = []
eng_name = ""
for item in raw_info:
    if "dark_text" in str(item):
        if "English:" in str(item.text):
            eng_name = item.text.strip().replace("English: ", "")
        name_info.append(item.text.strip())

