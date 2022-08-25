import requests
import bs4
import spotipy


#user_input = input("Which year would you like to travel to in YYY-MM-DD:")

URL = "https://www.billboard.com/charts/hot-100/2000-08-12/"

response = requests.get(URL)


soup = bs4.BeautifulSoup(response.text, "lxml")

first_list = [item.getText() for item in soup.find_all(name="h3" , class_="a-truncate-ellipsis")]

second_list = [item.replace('\n' , '') for item in first_list ]

title_list = [item.replace('\t' , '') for item in second_list ]



