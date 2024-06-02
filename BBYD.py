from tkinter import *
from tkinter import messagebox
from pytube import YouTube
import os
import moviepy.editor as mp
from PIL import Image


def download_audio():
    url = url_entry.get()
    yt = YouTube(url)
    audio_stream = yt.streams.filter(only_audio=True).order_by('abr').last()
    audio_file = audio_stream.download()
    output_name = output_name_entry.get()
    output_directory = r"F:\Youtube\Youtube Bytes\Python Audios"
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    output_path = os.path.join(output_directory, output_name + ".mp3")
    mp_audio = mp.AudioFileClip(audio_file)
    mp_audio.write_audiofile(output_path)
    os.remove(audio_file)
    messagebox.showinfo("Yeah, bitch!", "Audio file saved as " + output_path)


def download_video():
    url = url_entry.get()
    yt = YouTube(url)
    video_stream = yt.streams.filter(progressive=True).order_by('resolution').desc().first()
    output_name = output_name_entry.get()
    output_directory = r"F:\Youtube\Youtube Bytes\Python Videos"
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    output_path = os.path.join(output_directory, output_name + ".mp4")
    video_stream.download(output_path=output_path)
    messagebox.showinfo("Yeah, bitch!", "Video file saved as " + output_path)


def open_clip_window():
    url = url_entry.get()
    yt = YouTube(url)
    video_length = yt.length

    def clip_video():
        start_time = start_time_slider.get()
        end_time = end_time_slider.get()
        output_name = output_name_entry.get()
        output_directory = r"F:\Youtube\Youtube Bytes\Python Clips"
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)
        output_path = os.path.join(output_directory, output_name + "_clip.mp4")
        video_clip = mp.VideoFileClip(yt.streams.filter(progressive=True).order_by('resolution').desc().first().download()).subclip(start_time, end_time)
        video_clip.write_videofile(output_path)
        messagebox.showinfo("Yeah, bitch!", "Video clip saved as " + output_path)

    def update_time_labels(val):
        start_time = start_time_slider.get()
        end_time = end_time_slider.get()
        start_time_label.config(text=f"Start Time: {start_time // 3600:02}:{(start_time % 3600) // 60:02}:{start_time % 60:02}")
        end_time_label.config(text=f"End Time: {end_time // 3600:02}:{(end_time % 3600) // 60:02}:{end_time % 60:02}")

    clip_window = Toplevel(window)
    clip_window.title("Clip Video")
    clip_window.geometry("600x400")
    clip_window.configure(bg="#2C2C2C")

    fontStyle = ("Arial", 14, "bold")

    start_time_label = Label(clip_window, text="Start Time: 00:00:00", font=fontStyle, fg="white", bg="#2C2C2C")
    start_time_label.pack(pady=10)
    start_time_slider = Scale(clip_window, from_=0, to=video_length, orient=HORIZONTAL, length=500, font=fontStyle, bg="#4B4B4B", fg="white", bd=0, activebackground="#737373", command=update_time_labels)
    start_time_slider.pack(pady=10)

    end_time_label = Label(clip_window, text=f"End Time: {video_length // 3600:02}:{(video_length % 3600) // 60:02}:{video_length % 60:02}", font=fontStyle, fg="white", bg="#2C2C2C")
    end_time_label.pack(pady=10)
    end_time_slider = Scale(clip_window, from_=0, to=video_length, orient=HORIZONTAL, length=500, font=fontStyle, bg="#4B4B4B", fg="white", bd=0, activebackground="#737373", command=update_time_labels)
    end_time_slider.set(video_length)
    end_time_slider.pack(pady=10)

    clip_button = Button(clip_window, text="Clip Video, yo!", font=fontStyle, bg="#4B4B4B", fg="white", bd=0, padx=20, pady=10, activebackground="#737373", activeforeground="white", command=clip_video)
    clip_button.pack(pady=20)


def clear_data():
    url_entry.delete(0, END)
    output_name_entry.delete(0, END)


window = Tk()
window.title("Youtube Piracy Simulator (epic edition)")
window.geometry("600x500")
window.configure(bg="#2C2C2C")

fontStyle = ("Arial", 14, "bold")
entryfont = ("Century Schoolbook", 12)

logo = PhotoImage(file="F:\Youtube\Youtube Bytes\legacy folder\jesse.png")
logo_label = Label(window, image=logo, bg="#2C2C2C")
logo_label.place(relx=0.55, rely=0.6, anchor=CENTER)

url_label = Label(window, text="Enter the YouTube video URL yo!:", font=fontStyle, fg="white", bg="#2C2C2C")
url_label.pack()
url_entry = Entry(window, font=entryfont)
url_entry.pack(pady=10)

output_name_label = Label(window, text="Enter the desired name for the output file bitch!:", font=fontStyle, fg="white", bg="#2C2C2C")
output_name_label.pack()
output_name_entry = Entry(window, font=entryfont)
output_name_entry.pack(pady=10)

audio_button = Button(window, text="Download as Audio, yo!", font=fontStyle, bg="#4B4B4B", fg="white", bd=0, padx=20, pady=10, activebackground="#737373", activeforeground="white", command=download_audio)
audio_button.pack(pady=10)

video_button = Button(window, text="Download as Video, bitch!", font=fontStyle, bg="#4B4B4B", fg="white", bd=0, padx=20, pady=10, activebackground="#737373", activeforeground="white", command=download_video)
video_button.pack(pady=5)

clip_button_main = Button(window, text="Clip It", font=("Arial", 10), bg="#4B4B4B", fg="white", bd=0, padx=10, pady=5, activebackground="#737373", activeforeground="white", command=open_clip_window)
clip_button_main.pack(pady=10)

clear_button = Button(window, text="Clear", font=("Arial", 10), bg="#4B4B4B", fg="white", bd=0, padx=10, pady=5, activebackground="#737373", activeforeground="white", command=clear_data)
clear_button.pack(pady=10)

footer_label = Label(window, text="\"I am the one who knocks.\"", font=("Arial", 12), fg="white", bg="#2C2C2C")
footer_label.pack(side=BOTTOM, pady=10)

window.mainloop()
