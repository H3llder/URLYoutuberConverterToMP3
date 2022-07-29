# Só iniciar e adcionar o link na primeira e na segunda vez.
from pytube import YouTube
import os

# url = YouTube("https://www.youtube.com/watch?v=NvqxhJW_69I&ab_channel=LucasGabriel")

url = YouTube(str(input(">> ")))

while url:
    url = YouTube(str(input(">> ")))

    video = url.streams.filter(only_audio=True).first()

    destination = "/home/helder/Downloads/"
    out_file = video.download(output_path=destination)

    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

    print(url.title + " foi instalado com sucesso.")