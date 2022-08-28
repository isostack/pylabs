from spotipy.oauth2 import SpotifyOAuth
import spotipy
import requests
import bs4

# ====================== Top 100 billboard web scrapping ======================

#user_input = input("Which year would you like to travel to in YYY-MM-DD:")

# URL = "https://www.billboard.com/charts/hot-100/2000-08-12/"
# response = requests.get(URL)
# soup = bs4.BeautifulSoup(response.text, "lxml")
# first_list = [item.getText() for item in soup.find_all(name="h3" , class_="a-truncate-ellipsis")]
# second_list = [item.replace('\n' , '') for item in first_list ]
# title_list = [item.replace('\t' , '') for item in second_list ]

# ============================== Spotify API =================================
APP_CLIENT_ID = 'fdceaa19be54435a89ae9f101e148642'
APP_CLIENT_SECRET = '372a8cf15ccd4e9fab3a9b72f35e2b9c'
APP_REDIRECT_URI = 'http://example.com'


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=APP_CLIENT_ID,
        client_secret=APP_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]
# user-library-read
results = sp.current_user()
USER_ID = results['id']
print(USER_ID)