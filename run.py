from tkinter import filedialog
from tkinter import *
import YOLO
from tkinter import ttk
from tkinter import filedialog as fd
import tkinter as tk
from tkinter.messagebox import showinfo
import time
from PIL import ImageTk, Image
import threading

root = Tk()
root.title('YOLO VEditor')
root.resizable(False, False)
root.geometry('800x500')
filename = None
information_text = tk.StringVar()
information_text.set("Please choose mp4 file")


def select_file():
    global picture_label
    filetypes = (
        ('Video files', '*.mp4'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir=None,
        filetypes=filetypes)

    if filename:
        th = threading.Thread(target=YOLO.convert_the_video, args=(filename,picture_label,))
        th.start()

def pause_the_video():
    YOLO.paused = not YOLO.paused
    text = "|>" if YOLO.paused else "||"
    pause_button.configure(text=text)

def stop_the_video():
    YOLO.is_stopped = True

img = ImageTk.PhotoImage(Image.open("test.jpg"))
picture_label = ttk.Label(root, image=img)
open_button = ttk.Button(root, text='Open a File', command=select_file)
logo_label = ttk.Label(root, text="YOLO-VEditor", font=("Halvetica", 28))
pause_button = ttk.Button(root, text='||', command=pause_the_video)
stop_button = ttk.Button(root, text='STOP', command=stop_the_video)

logo_label.pack(expand=True)
open_button.pack(expand=True)
picture_label.pack(expand = True)
pause_button.pack()
stop_button.pack()

root.mainloop()
