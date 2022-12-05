#!/usr/bin/python3

## IMPORT LIBRARTY
from pytube import YouTube
import os, signal, sys
from colorama import init, Fore

## Ctrl + C
def def_hundler(sig, frame):
    print(Fore.RED + "\n\n[!] Exit...\n")
    sys.exit(1)
signal.signal(signal.SIGINT, def_hundler)

## Search in youtube
search = (str(input(Fore.GREEN + "\nInsert to search: ")))
key_word = search
html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + key_word)
video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
print(Fore.CYAN + "\nhttps://www.youtube.com/watch?v=" + video_ids[0])
print("https://www.youtube.com/watch?v=" + video_ids[1])
print("https://www.youtube.com/watch?v=" + video_ids[2])
print("https://www.youtube.com/watch?v=" + video_ids[3])
print("https://www.youtube.com/watch?v=" + video_ids[4])
print("https://www.youtube.com/watch?v=" + video_ids[5])

## URL INPUT USER
yt = YouTube(str(input(Fore.GREEN + "Enter the URL of the mp3 you want to download: \n>>\t")))

## EXTRACT ONLY AUDIO
mp3 = yt.streams.filter(only_audio=True).first()

## directory TO SAVE FILE
directory = (str(input(Fore.CYAN + "Enter the path of save file:\n>>\t")))

print(Fore.CYAN + "Download in your directory path\n>>\t" + directory)

## DOWNLOAD THE FILE
file_download = mp3.download(output_path=directory)

## SAVE THE FILE
base, ext = os.path.splitext(file_download)
new_file = base + '.mp3'
os.rename(file_download, new_file)

## RESULT OF SUCCESSFULLY DOWNLOAD AND SAVE FILE
print(Fore.GREEN + "Download Successfully\n>>\t" + yt.title)
