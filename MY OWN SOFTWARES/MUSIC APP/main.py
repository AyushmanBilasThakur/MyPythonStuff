import youtube_dl
import os
from sys import argv
from pydub import AudioSegment

# PROCESS OF CONVERSION
def process(f):
    audioIN = AudioSegment.from_file(f) 
    print("Processing.... " + str(f))
    audioIN.export(f[:-4] + "mp3", format="mp3")
    os.remove(f)

# CONFIG OF DOWNLOAD

download_config = {
    'format': 'bestaudio/best',
    'outtmpl': '%(title)s.%(ext)s',
    'nocheckcertificate': True,
    'postprocessor': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodedc': 'mp3',
        'preferredquality': '192',
    }],
}

# SONG DIRECTORY
if not os.path.exists('Songs'):
    os.mkdir('Songs')

os.chdir('Songs')


# DOWNLOADING
with youtube_dl.YoutubeDL(download_config) as dl:
    with open("../" + argv[1],'r') as f:
        for song_url in f:
            dl.download([song_url])

#CONVERSION
files = os.listdir(".")
for f in files:
    if f.lower()[-4:] == "webm":
        process(f)