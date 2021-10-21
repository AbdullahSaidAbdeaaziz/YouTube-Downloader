from pytube import *
from pytube import YouTube
from pytube.cli import on_progress

res = ["144p", "240p", "360p", "480p", "720p"]


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
                quality = str(input(f"Enter quality {res}: "))
                path = input(r"Enter Path to save video on it, Depend on (OS) {Linux, Windows, "
                             r"Mac} <'c:\Users\2011\balbal'>: ")
                print("Video is Downloading.........\n")
                video.streams.filter(progressive=True, res=quality).first().download(output_path=path)
                video.register_on_complete_callback(fin())
            else:
                print('Plz Enter valid Link!\n')
                continue
        elif choice == 2:
            playlist = input("Enter Link of Playlist: ")
            if playlist.startswith("h") and playlist.__contains__("playlist"):
                pl = Playlist(playlist)
                quality = input(f"Enter quality {res}: ")
                path = input(r"Enter Path to save Playlist on it, Depend on (OS) {Linux, Windows, "
                             r"Mac} <'c:\Users\2011\bal'>: ")
                print("Videos is Downloading.........\n")

                for ls in pl.videos:
                    ls.streams.get_by_resolution(quality).download(
                        output_path=path)
                    ls.register_on_complete_callback(fin())

            else:
                print('Plz Enter valid playlist Link!\n')
                continue
            ch = input("EXIT (y, n) >? ")[0]
        if ch == 'y':
            q = False


def main():
    menu()


if __name__ == '__main__':
    main()
