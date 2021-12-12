import os
import glob
import time

import cv2
import torch
import matplotlib.pyplot as plt
from PIL import ImageTk, Image

paused = False
is_stopped = False

def delete_redundant_files():
    files = glob.glob('results/*')
    for f in files:
        os.remove(f)
    os.rmdir("results/")

def convert_the_video(sample_video_dir="sample_video.mp4", picture_label=None):
    global is_stopped
    print(picture_label)
    cv2.startWindowThread()
    model = torch.hub.load('ultralytics/yolov5','yolov5l')
    cap = cv2.VideoCapture(sample_video_dir)
    ret, frame = cap.read()
    h, w = frame.shape[:2]
    out = cv2.VideoWriter("output.avi", cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 60, (w,h))
    out.write(frame)

    frame_number = 1
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == True and not is_stopped:
            print(is_stopped)
            frame_number += 1
            result = model([frame]).save("results/")
            while paused:
                time.sleep(1)
            # cv2.imshow('Frame', frame)
            img = Image.fromarray(frame).resize((444, 250), Image.ANTIALIAS)
            imgtk = ImageTk.PhotoImage(image = img)
            picture_label.configure(image=imgtk)
            out.write(frame)
        else:
            break
    is_stopped = False
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    delete_redundant_files()


