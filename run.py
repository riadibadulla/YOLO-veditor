from tkinter import filedialog
from tkinter import *
import YOLO

root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
if root.filename:
    YOLO.convert_the_video(root.filename)