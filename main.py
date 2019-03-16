import csv
import requests
from bs4 import BeautifulSoup

f = open("anime.csv", "w+")
f.write("name, eng_name, description, score, rating, duration, episode_num, genres, status, premiere_date, image_url\n")
f.close()

animes = ["Samurai Champloo", "Sword Art Online"]

for item in animes:

    item_url = item.replace(" ", "%20")

    url = "https://myanimelist.net/anime.php?q=" + item_url

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
    description = repr(soup.find("span", itemprop="description").text)
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

    anime_info = [name, eng_name, description, score, rating, duration, episode_num, genres, status, premiere_date, image_url]

    with open('anime.csv', 'a', newline='') as fd:
        wr = csv.writer(fd)
        wr.writerow(anime_info)


