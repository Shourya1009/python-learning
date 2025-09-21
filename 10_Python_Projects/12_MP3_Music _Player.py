
#  Install Dependencies : - pip install pygame tk
  
import tkinter as tk
from tkinter import filedialog
import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Functions
def load_music():
    file = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])
    if file:
        music_file.set(file)
        pygame.mixer.music.load(file)
        song_label.config(text=f"Loaded: {file.split('/')[-1]}")

def play_music():
    pygame.mixer.music.play()
    song_label.config(text="Playing...")

def pause_music():
    pygame.mixer.music.pause()
    song_label.config(text="Paused")

def resume_music():
    pygame.mixer.music.unpause()
    song_label.config(text="Resumed")

def stop_music():
    pygame.mixer.music.stop()
    song_label.config(text="Stopped")

# GUI Window
root = tk.Tk()
root.title("🎵 Simple MP3 Player")
root.geometry("400x250")

music_file = tk.StringVar()

# Widgets
song_label = tk.Label(root, text="No song loaded", font=("Arial", 12))
song_label.pack(pady=10)

btn_load = tk.Button(root, text="Load Song", command=load_music, width=15)
btn_load.pack(pady=5)

btn_play = tk.Button(root, text="Play", command=play_music, width=15, bg="green", fg="white")
btn_play.pack(pady=5)

btn_pause = tk.Button(root, text="Pause", command=pause_music, width=15, bg="orange")
btn_pause.pack(pady=5)

btn_resume = tk.Button(root, text="Resume", command=resume_music, width=15, bg="blue", fg="white")
btn_resume.pack(pady=5)

btn_stop = tk.Button(root, text="Stop", command=stop_music, width=15, bg="red", fg="white")
btn_stop.pack(pady=5)

# Run GUI
root.mainloop()
