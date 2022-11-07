from os import path
from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube
import shutil

# FUNCTIONS


def select_path():
    # allows user to select a path from the explorer
    path = filedialog.askdirectory()
    path_label.config(text=path)


def download_file():
    # get user path
    get_link = link_field.get()
    # get selecetd path
    screen.title("Downloading...")
    user_path = path_label.cget("text")
    # download video
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()
    # move to selected directory
    shutil.move(mp4_video, user_path)
    screen.title("Download Complete! Download another file...")


screen = Tk()
title = screen.title("YouTube Downloader")
canvas = Canvas(screen, width=500, height=500)
canvas.pack()

# image logo
logo_img = PhotoImage(file='yt.png')
# resizing the image
logo_img = logo_img.subsample(2, 2)
canvas.create_image(250, 80, image=logo_img)

# link field
link_field = Entry(screen, width=50)
link_label = Label(screen, text='Enter Download Link:', font=('Arial', 15))

# add widgets to window
canvas.create_window(250, 170, window=link_label)
canvas.create_window(250, 220, window=link_field)

# Select PATH for saving the file
path_label = Label(screen, text='Select PATH for download')
select_btn = Button(screen, text='Select', command=select_path)
# Add to winodow
canvas.create_window(250, 280, window=path_label)
canvas.create_window(250, 330, window=select_btn)

# Download button
download_btn = Button(screen, text='Download File',
                      font=('Arial', 15), command=download_file)
# add to canvas
canvas.create_window(250, 400, window=download_btn)


screen.mainloop()
