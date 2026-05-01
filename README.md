# TerminalLyrics
Lyrics synced to Spotify inside your terminal 

## Important Notice
In order for this to work you need a Spotify Premium Account, or else the Spotify API won't work.

## Installation
### Prerequisites
Visit [Spotify's Developer Dashboard](https://developer.spotify.com/dashboard) and click on "Create app"  .
You can write whatever you want as the name and description. 
I recommend writing ```https://spotify.com/en/account/overview``` as a redirect URI.  
Make sure to tick the "Web API" box when asked "Which API/SDKs are you planning to use?". After that create the app.  
When the app is created, copy the Client ID and Client Secret. Paste both of them in a file called '.env' using the format down below in the directory the executable or the script will be in.  
```
SPOTIFY_SECRET=
SPOTIFY_ID=
```
### Windows Executable
If you want the program as an executable, download the latest version on the 'Releases' tab.  
Simply put it in a directory with the '.env' file together and you're good to go.  
(All the steps after here are usually clear, but if you need help, skip down to 'First Run')
### Running from Source
Download the source and create a venv, you'll need following packages ```lrclib-python spotipy dotenv-python```.
### First Run
On your first run (and likely on some runs ins the future too), your browser will open a spotify website, copy the link first and then click accept.  
Now paste the link into the terminal where you are asked to paste the link in and press enter.  
(A .cache file will be created, this is important so you don't have to paste the link everytime you run the program, so leave the file alone and don't delete it.)  
There should now be lyrics from your song playing on spotify. (sometimes, it may take a few seconds to get the lyrics)

## Notes
- I used [lrclib](https://lrclib.net/) get the lyrics. The lyrics on there are community made, so they might be wrong sometimes or the timing of the sync is off.
  I already have plans to make an 'import lyrics' feature, so the process to get the lyrics are faster and you can override wrong lyrics, but I have no idea when to implement this.
- I coded the current version on a friday evening, so there might be things that are buggy or can be improved (making it take less resources for example)
- If you have any problems or so you can contact me on twitter and discord https://benno.nekoweb.org/contact/
