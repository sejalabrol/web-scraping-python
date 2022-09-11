import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Fetching environment variables
load_dotenv()
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

date = input(
    "Which year do you want to travel to? (Type the date in this format YYYY-MM-DD):\n"
)

# Billboard Hot 100 website
URL = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(URL)
contents = response.text

# Parsing the website to get the song names
# https://beautiful-soup-4.readthedocs.io/en/latest/
soup = BeautifulSoup(contents, "html.parser")
songs = [
    song.getText().split("\n")[1]
    for song in soup.find_all(
        name="h3",
        class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only",
    )
]


# Authenticating Spotify using the Spotipy Python Library
# https://spotipy.readthedocs.io/en/2.19.0/
# https://developer.spotify.com/

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
    )
)
user_id = sp.current_user()["id"]

# Creating a new Playlist
playlist = sp.user_playlist_create(
    user=user_id,
    name=f"Billboard {date}",
    public=False,
    collaborative=False,
    description=f"Songs from Billboard Hot 100 on {date}",
)

playlist_id = playlist["id"]

# Fetching the song URIs to create a playlist
song_uris = []
for song in songs:
    try:
        track = sp.search(q=song, limit=1, offset=0, type="track", market=None)
        song_uri = track["tracks"]["items"][0]["uri"]
        song_uris.append(song_uri)
    except:
        pass

# Adding the songs to the created playlist
sp.user_playlist_add_tracks(
    user=user_id, playlist_id=playlist_id, tracks=song_uris, position=None
)
