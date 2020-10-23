from pytube import YouTube
from win10toast import ToastNotifier


def last_ned():
    link = input("Skriv linken: ")
    yt = YouTube(link)

    print("Tittel: ", yt.title)
    print("Antall visninger: ", yt.views, "\n")

    ys = yt.streams.get_highest_resolution()

    print("Laster ned...")
    ys.download(r'C:\Users\trymk\Desktop')
    toaster = ToastNotifier()
    toaster.show_toast("Fullført", "Filen ligger på skrivebordet ditt")


last_ned()
