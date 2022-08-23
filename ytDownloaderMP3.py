#!/usr/bin/python3

## IMPORT LIBRARTY
from pytube import YouTube
import os

## URL INPUT USER
yt = YouTube(str(input("Enter the URL of the mp3 you want to download: \n>>\t")))

## EXTRACT ONLY AUDIO
mp3 = yt.streams.filter(only_audio=True).first()

## directory TO SAVE FILE
directory = (str(input("Enter the path of save file:\n>>\t")))

print("Download in your directory path\n>>\t" + directory)

## DOWNLOAD THE FILE
file_download = mp3.download(output_path=directory)

## SAVE THE FILE
base, ext = os.path.splitext(file_download)
new_file = base + '.mp3'
os.rename(file_download, new_file)

## RESULT OF SUCCESSFULLY DOWNLOAD AND SAVE FILE
print("Download Successfully\n>>\t" + yt.title)
