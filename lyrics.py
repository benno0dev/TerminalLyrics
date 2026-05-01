import re
import lrclib
import os

lrc = lrclib.LrclibClient()

songCache = ""
lyricCache = ""

def getTimes(lyrics):
    pattern = re.compile(r"\[(\d{2}):(\d{2})\.(\d{2})\]")

    times = []
    for m in pattern.finditer(lyrics):
        minutes, seconds, centis = map(int, m.groups())
        ms = minutes * 60000 + seconds * 1000 + centis * 10
        times.append(ms)
    return times

def getPlainLyrics(lyrics):
    lyrics_plain = re.sub(r"\[\d{2}:\d{2}\.\d{2}\]\s*", "", lyrics)
    return lyrics_plain

def getLineInt(times, progress):
    line = 0
    for count, time in enumerate(times):
        if time < progress:
            line = count
            continue
        else:
            break
    return line

def getLineStr(songName, artistName, songDuration, progress):
    global lyricCache, songCache
    if songName == songCache and lyricCache != "":
        lyrics = lyricCache
    else:
        lyrics = lrc.get(id_name=songName, artist_name=artistName, duration=songDuration).lyrics
        lyricCache = lyrics
        songCache = songName
    if lyrics == None:
        line = "No lyrics found."
    elif "[" in lyrics and "]" in lyrics:
        try:
            line = getPlainLyrics(lyrics).splitlines(False)[getLineInt(getTimes(lyrics), progress)]
        except IndexError:
            line = ""
            if os.name == 'nt':
                _ = os.system('cls')
            else:
                _ = os.system('clear')
    else:
        line = lyrics
    return line, lyrics