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

def clip_video():
    url = url_entry.get()
    yt = YouTube(url)
    video_stream = yt.streams.filter(progressive=True).order_by('resolution').desc().first()
    video_file = video_stream.download()
    start_time = start_time_entry.get()
    end_time = end_time_entry.get()
    output_name = output_name_entry.get()
    output_directory = r"F:\Youtube\Youtube Bytes\Python Clips"
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    output_path = os.path.join(output_directory, output_name + "_clip.mp4")
    video_clip = mp.VideoFileClip(video_file).subclip(start_time, end_time)
    video_clip.write_videofile(output_path)
    os.remove(video_file)
    messagebox.showinfo("Yeah, bitch!", "Video clip saved as " + output_path)

def clear_data():
    url_entry.delete(0, END)
    output_name_entry.delete(0, END)
    start_time_entry.delete(0, END)
    end_time_entry.delete(0, END)

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

clip_label = Label(window, text="Clip Video Section:", font=fontStyle, fg="white", bg="#2C2C2C")
clip_label.pack(pady=10)

start_time_label = Label(window, text="Start Time (hh:mm:ss):", font=fontStyle, fg="white", bg="#2C2C2C")
start_time_label.pack()
start_time_entry = Entry(window, font=entryfont)
start_time_entry.pack(pady=5)

end_time_label = Label(window, text="End Time (hh:mm:ss):", font=fontStyle, fg="white", bg="#2C2C2C")
end_time_label.pack()
end_time_entry = Entry(window, font=entryfont)
end_time_entry.pack(pady=5)

clip_button = Button(window, text="Clip Video, yo!", font=fontStyle, bg="#4B4B4B", fg="white", bd=0, padx=20, pady=10, activebackground="#737373", activeforeground="white", command=clip_video)
clip_button.pack(pady=10)

clear_button = Button(window, text="Clear", font=("Arial", 10), bg="#4B4B4B", fg="white", bd=0, padx=10, pady=5, activebackground="#737373", activeforeground="white", command=clear_data)
clear_button.pack(pady=10)

footer_label = Label(window, text="\"I am the one who knocks.\"", font=("Arial", 12), fg="white", bg="#2C2C2C")
footer_label.pack(side=BOTTOM, pady=10)

window.mainloop()
