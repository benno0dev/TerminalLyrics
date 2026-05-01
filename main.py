import lyrics
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv
import time

load_dotenv()

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.getenv("SPOTIFY_ID"),
                                               client_secret=os.getenv("SPOTIFY_SECRET"),
                                               redirect_uri="https://spotify.com/de/account/overview",
                                               scope="user-read-playback-state"))

lastLyricLine = ""

def main():
    global lastLyricLine
    results = sp.current_playback()
    if results != None:
        id_name = results["item"]["name"]
        artist_name = results["item"]["artists"][0]["name"]
        duration = (results["item"]["duration_ms"] / 1000)
        progress = results["progress_ms"]
        lyricLine = lyrics.getLineStr(id_name, artist_name, duration, progress)[0]
        if lyricLine != lastLyricLine:
            lastLyricLine = lyricLine
            print(lyricLine)
    else:
        print("Not playing a song")

while True:
    main()
    time.sleep(1)