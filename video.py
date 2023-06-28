from tkinter import *
from tkinter import filedialog
from pytube import YouTube
from moviepy.editor import *
import shutil


def Download():
    url = url_entry.get()
    video_path = path_label.cget("text")
    video = YouTube(url).streams.get_highest_resolution().download()
    video_clip = VideoFileClip(video)
    # cnv to mp3
    audio_file = video_clip.audio
    audio_file.write_audiofile('audio.mp3')
    audio_file.close()
    shutil.move('audio.mp3', video_path)
    # cnv to mp3
    video_clip.close()
    shutil.move(video, video_path)


def GetPath():
    path = filedialog.askdirectory()
    path_label.config(text=path)


root = Tk()
root.title("YouTube Video Downloader")

canvas = Canvas(root, width=400, height=400)
canvas.pack()

# app name
app_label = Label(root, text="YouTube Video Downloader",
                  fg='red', font=('Arial', 15))
canvas.create_window(205, 50, window=app_label)

url_label = Label(root, text="Enter The URL Of The YouTube Video: ")
url_entry = Entry(root)
canvas.create_window(205, 100, window=url_label)
canvas.create_window(205, 130, window=url_entry)

path_label = Label(root, text="Select Path to Download")
path_btn = Button(root, text="Select", command=GetPath)
canvas.create_window(205, 160, window=path_label)
canvas.create_window(205, 190, window=path_btn)

download_btn = Button(root, text="Download", command=Download)
canvas.create_window(205, 230, window=download_btn)

root.mainloop()
