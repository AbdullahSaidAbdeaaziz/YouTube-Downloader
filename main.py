import tkinter

from pytube import *
from pytube import YouTube
from pytube.cli import on_progress
from tkinter import Tk
from tkinter.filedialog import askdirectory
res = ["144p", "240p", "360p", "480p", "720p"]
all_res = []
f_p = set()


def fin() -> None:
    print("Done!")


def menu() -> None:
    print("\t\tYouTube Downloader\n==================")
    print("1) one video.\n"
          "2) playlist.\n")
    q = True
    while q:
        choice = int(input("choice (1, 2) : "))
        if choice == 1:
            link = str(input("Enter Link of Video: "))
            if link.startswith("h") and link.__contains__("watch"):
                video = YouTube(link, on_progress_callback=on_progress)

                for l in res:
                    check = video.streams.get_by_resolution(l)
                    if check is not None:
                        all_res.append(l)

                quality = str(input(f"Enter quality {all_res}: "))
                if quality not in res:
                    print("sorry this is Quality not available.\n")
                    quality = str(input(f"Enter quality {all_res}: "))
                    print("choose place 😀")
                path = askdirectory(title='Select Folder')
                tkinter.Tk().withdraw()
                print("Video is Downloading.........\n")

                video.streams.get_by_resolution(quality).download(output_path=path)
                video.register_on_complete_callback(fin())
            else:
                print('Plz Enter valid Link!\n')
                continue
        elif choice == 2:
            playlist = input("Enter Link of Playlist: ")
            if playlist.startswith("h") and playlist.__contains__("playlist"):
                pl = Playlist(playlist)

                for ls in pl.videos:
                    for quality in res:
                        if ls.streams.get_by_resolution(quality) is not None:
                            f_p.add(quality)
                quality = input(f"Enter quality {f_p}: ")
                if quality not in f_p:
                    print("sorry this is Quality not available for all Videos.\n")
                    quality = input(f"Enter quality {f_p}: ")
                path = askdirectory(title='Select Folder')
                tkinter.Tk().withdraw()

                print("Videos is Downloading.........\n")

                for ls in pl.videos:
                    ls.streams.get_by_resolution(quality).download(
                        output_path=path)
                    ls.register_on_complete_callback(fin())

            else:
                print('Plz Enter valid playlist Link!\n')
                continue
        ch = input("EXIT (y, n) >? ")
        if ch == 'y':
            q = False


def main():
    menu()


if __name__ == '__main__':
    main()
