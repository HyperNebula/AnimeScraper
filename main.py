import csv
import requests
from bs4 import BeautifulSoup

f = open("anime.csv", "w+")
f.write("name, eng_name, description, score, rating, duration, episode_num, genres, status, premiere_date, image_url\n")
f.close()

animes = ["Samurai Champloo", "Sword Art Online"]

for show in animes:

    item_url = show.replace(" ", "%20")

    url = "https://myanimelist.net/anime.php?q=" + item_url

    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    result = soup.find(class_='hoverinfo_trigger fw-b fl-l')
    result_link = result['href']

    url = result_link

    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    name = soup.find("span", itemprop="name")
    image_url = soup.find("img", itemprop="image")
    description = repr(soup.find("span", itemprop="description"))
    score = soup.find("span", itemprop="ratingValue")

    rating = str(soup.find(text="Rating:").parent.parent).replace("Rating:", "")
    eng_name = str(soup.find(text="English:").parent.parent).replace("English:", "")
    duration = str(soup.find(text="Duration:").parent.parent).replace("Duration:", "")
    genres = str(soup.find(text="Genres:").parent.parent).replace("Genres:", "")
    status = str(soup.find(text="Status:").parent.parent).replace("Status:", "")
    episode_num = str(soup.find(text="Episodes:").parent.parent).replace("Episodes:", "")
    premiere_date = str(soup.find(text="Premiered:").parent.parent).replace("Premiered:", "")

    anime_info = [name, eng_name, description, score, rating, duration, episode_num, genres, status, premiere_date, image_url]

    with open('anime.csv', 'a', newline='') as fd:
        wr = csv.writer(fd)
        wr.writerow(anime_info)


