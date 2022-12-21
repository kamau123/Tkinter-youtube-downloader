from tkinter import *
from tkinter import filedialog
from pytube import *
from moviepy.editor import VideoFileClip
import shutil
# functions


def select_path():
    # allow user to select path
    path = filedialog.askdirectory()
    path_label.config(text=path)


def download_file():
    # get user path
    get_link = link_field.get()
    # get selected path
    user_path = path_label.cget('text')
    # download video
    screen.title('downloading')
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()
    # move to selected path
    shutil.move(mp4_video,user_path)
    screen.title('Download Complete!! download another file?')


screen = Tk()
title = screen.title('Youtube Video Downloader')
canvas = Canvas(screen, width=500, height=500)
canvas.pack()

# image logo

logo_img = PhotoImage(file='yt.png')

# resize image

logo_img = logo_img.subsample(2, 2)

canvas.create_image(250, 80, image=logo_img)

#link field

link_field = Entry(screen, width=50)
link_label = Label(screen, text=' Enter Youtube Video Link', font=['Arial', 15])

# select path
path_label = Label(screen, text='Select Download Location', font=['Arial', 15])
select_btn = Button(screen, text='Select', command=select_path)

# add to window
canvas.create_window(250, 280, window=path_label)
canvas.create_window(250, 330, window=select_btn)

# add widgets to window

canvas.create_window(250, 170, window=link_label)
canvas.create_window(250, 220, window=link_field)

# download buttons

download_btn = Button(screen, text='Download Video', command=download_file)
# add to canvas

canvas.create_window(250, 390, window=download_btn)

screen.mainloop()
