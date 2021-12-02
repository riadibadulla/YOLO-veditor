import cv2
import torch

model = torch.hub.load('ultralytics/yolov5','yolov5s')
sample_video_dir = "sample_video.mp4"
cap = cv2.VideoCapture(sample_video_dir)

out = cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (1280,720))


frame_number = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    frame_number+=1
    if ret == True:
        # cv2.imshow('Frame',frame)
        result = model([frame]).save("results/")
        # cv2.imshow('Frame',frame)
        print(frame_number/120)
        out.write(frame)
        # Press Q on keyboard to  exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
        if frame_number/120>15:
            break
            # Break the loop
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()


