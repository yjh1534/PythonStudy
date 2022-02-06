from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date_to_travel = input("Which date do you want to travel? YYYY-MM-DD: ")

#Get html text
URL = f"https://www.billboard.com/charts/hot-100/{date_to_travel}/"
webpage = requests.get(URL)

#create soup & get information
soup = BeautifulSoup(webpage.content, "html.parser")

songs = soup.select(".o-chart-results-list-row-container ul #title-of-a-story")

titles = [song.getText()[1:-1] for song in songs]
artists = [song.next_sibling.next_sibling.getText()[:-1] for song in songs]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id="17e9a403e3644cf8b5e6bdb0df353aa6",
        client_secret="74efdee84750445d98bc9664997a683f",
        redirect_uri="http://example.com",
        scope="playlist-modify-private",
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

song_uris = []
for i in range(100):
    result = sp.search(q=f"track:{titles[i]}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{titles[i]} is skipped")
        
playlist = sp.user_playlist_create(user=user_id, name=f"{date_to_travel} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)