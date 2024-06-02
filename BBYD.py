from tkinter import *
from tkinter import messagebox
from pytube import YouTube
import os
import moviepy.editor as mp
from PIL import Image


def download_audio():
    # Get the YouTube video URL, bitch!
    url = url_entry.get()

    # Create a YouTube object
    yt = YouTube(url)

    # Select the highest quality audio stream, yo!
    audio_stream = yt.streams.filter(only_audio=True).order_by('abr').last()

    # Download the audio stream, bitch!
    audio_file = audio_stream.download()

    # Get the desired name for the output audio file from the user, bitch!
    output_name = output_name_entry.get()

    # Specify the full path to the output file and save the audio file there, yo!
    output_directory = r"F:\Youtube\Youtube Bytes\Python Audios"
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    output_path = os.path.join(output_directory, output_name + ".mp3")

    # Convert the audio file to mp3 and save to the output path, yo!
    mp_audio = mp.AudioFileClip(audio_file)
    mp_audio.write_audiofile(output_path)

    # Delete the original audio file, bitch!
    os.remove(audio_file)

    # Show a success message, yo!
    messagebox.showinfo("Yeah, bitch!", "Audio file saved as " + output_path)

def download_video():
    # Get the YouTube video URL, bitch!
    url = url_entry.get()

    # Create a YouTube object
    yt = YouTube(url)

    # Select the highest quality video stream, yo!
    video_stream = yt.streams.filter(progressive=True).order_by('resolution').desc().first()

    # Get the desired name for the output video file from the user, bitch!
    output_name = output_name_entry.get()

    # Specify the full path to the output file and save the video file there, yo!
    output_directory = r"F:\Youtube\Youtube Bytes\Python Videos"
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    output_path = os.path.join(output_directory, output_name + ".mp4")

    # Download the video stream directly to the output file, bitch!
    video_stream.download(output_path=output_path)

    # Show a success message, yo!
    messagebox.showinfo("Yeah, bitch!", "Video file saved as " + output_path)

# Function to clear the entered data
def clear_data():
    url_entry.delete(0, END)  # Clear the URL entry field
    output_name_entry.delete(0, END)  # Clear the output name entry field


# Create the main window, yo!
window = Tk()
window.title("Youtube Piracy Simulator (epic edition)")
window.geometry("600x400")
window.configure(bg="#2C2C2C")

# Set the font style and size, yo!
fontStyle = ("Arial", 14, "bold")
entryfont = ("Century Schoolbook", 12)

# Add the Breaking Bad logo, bitch!
logo = PhotoImage(file="F:\Youtube\Youtube Bytes\legacy folder\jesse.png")
logo_label = Label(window, image=logo, bg="#2C2C2C")
logo_label.place(relx=0.55, rely=0.6, anchor=CENTER)

# Create the URL input field, bitch!
url_label = Label(window, text="Enter the YouTube video URL yo!:", font=fontStyle, fg="white", bg="#2C2C2C", highlightbackground="#4B4B4B", highlightcolor="#4B4B4B", highlightthickness=2)
url_label.pack()
url_entry = Entry(window, font=entryfont, highlightthickness=0, highlightbackground="#2C2C2C")
url_entry.pack(pady=10)

# Create the output name input field, yo!
output_name_label = Label(window, text="Enter the desired name for the output file bitch!:", font=fontStyle, fg="white", bg="#2C2C2C", highlightbackground="#4B4B4B", highlightcolor="#4B4B4B", highlightthickness=2)
output_name_label.pack()
output_name_entry = Entry(window, font=entryfont, highlightthickness=0, highlightbackground="#2C2C2C")
output_name_entry.pack(pady=10)

# Create the audio download button, bitch!
audio_button = Button(window, text="Download as Audio, yo!", font=fontStyle, bg="#4B4B4B", fg="white", bd=0, padx=20, pady=10, activebackground="#737373", activeforeground="white", command=download_audio)
audio_button.pack(pady=10)

# Create the video download button, yo!
video_button = Button(window, text="Download as Video, bitch!", font=fontStyle, bg="#4B4B4B", fg="white", bd=0, padx=20, pady=10, activebackground="#737373", activeforeground="white", command=download_video)
video_button.pack(pady=5)

# Create the Clear button with smaller size and font
clear_button = Button(window, text="Clear", font=("Arial", 10), bg="#4B4B4B", fg="white", bd=0, padx=10, pady=5, activebackground="#737373", activeforeground="white", command=clear_data)
clear_button.pack(pady=10)

# Add a footer with a quote from the show, bitch!
footer_label = Label(window, text="\"I am the one who knocks.\"", font=("Arial", 12), fg="white", bg="#2C2C2C")
footer_label.pack(side=BOTTOM, pady=10)
# Run the main event loop, yo!
window.mainloop()
