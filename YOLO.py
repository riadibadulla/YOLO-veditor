import os
import glob
import cv2
import torch
import matplotlib.pyplot as plt

def delete_redundant_files():
    files = glob.glob('results/*')
    for f in files:
        os.remove(f)
    os.rmdir("results/")

def convert_the_video(sample_video_dir="sample_video.mp4"):
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
        if ret == True:
            frame_number += 1
            result = model([frame]).save("results/")
            cv2.imshow('Frame', frame)
            print(frame_number)
            out.write(frame)
            # Press Q on keyboard to  exit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
                # Break the loop
        else:
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()
    delete_redundant_files()


