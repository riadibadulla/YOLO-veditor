from tkinter import filedialog
from tkinter import *
import YOLO
from tkinter import ttk
from tkinter import filedialog as fd
import tkinter as tk
from tkinter.messagebox import showinfo
import time

root = Tk()
root.title('YOLO VEditor')
root.resizable(False, False)
root.geometry('500x150')
filename = None
information_text = tk.StringVar()
information_text.set("Please choose mp4 file")

def select_file():
    filetypes = (
        ('Video files', '*.mp4'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir=None,
        filetypes=filetypes)

    if filename:
        information_text.set("Press \"q\" to quit")
        time.sleep(1)
        YOLO.convert_the_video(filename)



open_button = ttk.Button(root, text='Open a File', command=select_file)
logo_label = ttk.Label(root, text="YOLO-VEditor", font=("Halvetica", 28))
information_label = ttk.Label(root, textvariable=information_text, font=("Arial", 9))

logo_label.pack(expand=True)
open_button.pack(expand=True)
information_label.pack()


root.mainloop()
# root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("all files","*.*")))


