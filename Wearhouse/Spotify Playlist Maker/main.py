from curses.ascii import US
from spotipy.oauth2 import SpotifyOAuth
import spotipy
import requests
import bs4

# ====================== Top 100 billboard web scrapping ======================
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

URL = f"https://billboard.com/charts/hot-100/2020-01-01"
response = requests.get(URL)
soup = bs4.BeautifulSoup(response.text, "lxml")
first_list = [item.getText() for item in soup.find_all(name="h3" , class_="a-truncate-ellipsis")]
second_list = [item.replace('\n' , '') for item in first_list ]
title_list = [item.replace('\t' , '') for item in second_list ]

# ============================== Spotify API =================================

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        #client_id=APP_CLIENT_ID,
        #client_secret=APP_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]
# user-library-read
results = sp.current_user()
USER_ID = results['id']

song_uris = []

for title in title_list:
    search = sp.search(q=f"track:{title}", type="track")
    try:
        uri = search['tracks']['items'][0]['uri']
        song_uris.append(uri)
        print("found")
    except IndexError:
        print(f"{title} not found. Skipped.")

PLAYLIST_ID = sp.user_playlist_create(user=USER_ID,public=False,name=f"{date} BillBoard-100")['id']

sp.user_playlist_add_tracks(playlist_id=PLAYLIST_ID,tracks=song_uris,user=USER_ID)