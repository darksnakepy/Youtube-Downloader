from pytube import YouTube, Playlist
import sys 
from tkinter import Tk 
from tkinter.filedialog import askdirectory


def choosePath():
    Tk().withdraw() 
    path = askdirectory() 

    return path
    


def downloadingVidmp4(url):
    ytDw = YouTube(str(url))
    try:
        dwLink = ytDw.streams.filter(progressive=True).last()
        print("Select a folder")
        path = choosePath()
        dwLink.download(path)
    except Exception as e:
        print(e)
        sys.exit(1)


def downloadingAudio(url):
    ytDw = YouTube(str(url))
    try:
        audio = ytDw.streams.filter(only_audio=True).last()
        print("Select a folder")
        path = choosePath()
        audio.download(path)
    except Exception as e:
        print(e)
        sys.exit(1)
    

def downloadPlaylist(url):
    plDw = Playlist(str(url))
    try:
        for video in plDw.videos:
            playlist = video.streams.filter(progressive=True).last()
            print("Select a folder")
            path = choosePath()
            playlist.download(path)
    except Exception as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    while(True):
        answer = int(input("""Choose an option:

        [1] Download a video from Youtube (Mp4)

        [2] Download an audio from Youtube (Mp3)

        [3] Download a playlist
        
        [4] Exit

        > """))

        if(answer == 1):
            inputUrl = input("Insert a youtube video link: ")
            downloadingVidmp4(inputUrl)
            print("Done!\n")

        elif(answer==2):
            inputUrlAudio = input("Insert a youtube video link: ")
            downloadingAudio(inputUrlAudio)
            print("Done!\n")

        elif(answer==3):
            inputPlaylist = input("Insert a youtube's playlist link: ")
            downloadPlaylist(inputPlaylist)
            print("Done!\n")

        elif(answer == 4):
            sys.exit(1)

        else:
            print("Wrong choice.")


     





