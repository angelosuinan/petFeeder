import cv2
from cv2 import *
import sys
import time
import datetime
import os
from time import sleep

class Cam(object):

    def start(self):
        with open('assets/run.txt', 'r') as f:
            if f.readline()=='1':
                return
        with open('assets/run.txt', 'w+') as f:
            f.write("1")
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalcatface_extended.xml")
        video_capture = cv2.VideoCapture(0)
        while True:
        # Capture frame-by-frame
            ret, frame = video_capture.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(
                gray,
            scaleFactor=1.5,
            minNeighbors=13,
            minSize=(50, 50),
            flags=cv2.CASCADE_SCALE_IMAGE
            )
            # Draw a rectangle around the faces¬
           # for (x, y, w, h) in faces:¬
          #      cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)¬
            if len(faces) > 0:
                print("FOUND IT")
                with open('assets/feed.txt', 'w+') as f:
                    f.write("1")
                sleep(20)
                with open('assets/feed.txt', 'w+') as f:
                    f.write("0")
            cv2.imwrite("assets/images/live.jpg", frame )
            # Display the resulting frame
          #  cv2.imshow('Video', frame)
            print ("Found " + str(len(faces)) + " cat face/s")
        # When everything is done, release the capture
        video_capture.release()
        cv2.destroyAllWindows()
