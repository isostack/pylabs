import requests
import bs4

URL = "https://site.gctu.edu.gh"

response = requests.get(URL)

web_page = response.text

soup = bs4.BeautifulSoup(web_page, "html.parser")

print(soup.prettify())

all_movies = soup.find("table")

print(all_movies)



