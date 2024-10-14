import os
import tkinter as tk
from tkinter import filedialog
from pydub import AudioSegment

def draw_widgets():
    drop_down.place(x=95, y=150)
    button.place(x=120, y=190)

def rem_widgets():
    drop_down.place_forget()
    button.place_forget()

def original_label():
    label.config(text=orig_label)

def revert_label(text):
    label.config(text=text)
    root.after(2000, original_label)

def browse_file():
    return filedialog.askopenfilename()

def browse_dir():
    return filedialog.askdirectory()

def pinili():
    return selected_option.get()

def on_click():
    rem_widgets()
    if pinili() == options[0]:
        mp3_to_wav()
    else:
        wav_to_mp3()
    draw_widgets()

def mp3_to_wav():
    label.config(text="Select a\nmp3!")
    mp3_file = browse_file()
    if not mp3_file:
        label.config(text=orig_label)
        return
    if mp3_file.find("mp3") == -1:
        revert_label("Not a MP3!")
        return
    mp3_str = os.path.basename(mp3_file)
    label.config(text="Where to\nsave?")
    wav_dir = browse_dir()
    if not wav_dir:
        label.config(text=orig_label)
        return
    wav_mp3 = os.path.join(wav_dir, mp3_str)
    # para iwas error
    wav_path_now = os.path.normpath(wav_mp3)
    mp3_wav_file = os.path.join(wav_path_now)
    wav_file = os.path.splitext(mp3_wav_file)[0] + ".wav"
    wav = AudioSegment.from_file(mp3_file)
    wav.export(wav_file, format='wav')
    revert_label(f"Convert complete!")

def wav_to_mp3():
    label.config(text="Select a\nwav!")
    wav_file = browse_file()
    if not wav_file:
        label.config(text=orig_label)
        return
    if wav_file.find("wav") == -1:
        revert_label("Not a wav file")
        return
    wav_str = os.path.basename(wav_file)
    label.config(text="Where to\nsave?")
    mp3_dir = browse_dir()
    if not mp3_dir:
        label.config(text=orig_label)
        return
    mp3_wav = os.path.join(mp3_dir, wav_str)
    mp3_path_corrected = os.path.normpath(mp3_wav)
    mp3_file = os.path.splitext(mp3_path_corrected)[0] + ".mp3"
    mp3 = AudioSegment.from_file(wav_file)
    mp3.export(mp3_file, format="mp3")
    revert_label("Conversion complete!")

root = tk.Tk()
root.title("Converter")
root.geometry("300x300")
root.resizable(False, False)


options = ["Mp3 to WAV", "WAV to Mp3"]

orig_label = "Choose a Converter:"
label = tk.Label(root, text=orig_label, font=("Courier", 15))
label.place(x=40, y=90)

selected_option = tk.StringVar()
selected_option.set(options[0])


drop_down = tk.OptionMenu(root, selected_option, *options)

button = tk.Button(root, text="Convert!",command=on_click)

draw_widgets()

root.mainloop()