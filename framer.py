import cv2, time
import numpy as np
import logging
import threading
import concurrent.futures

import multiprocessing
from multiprocessing import Process, Manager
import os, sys

import simpleaudio as sa
import matplotlib.pyplot as plt
from scipy.io.wavfile import write

waves = {}

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

# Opens the Video file
cap=cv2.VideoCapture('D:/Users\kmont\Documents\ExperimentalSound\ShadowGraph_Phoebus_Mach2.mp4')
num_of_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) #1586

def open_frame(frame_no):
    while(cap.isOpened()):
        cap.set(1,frame_no)
        ret, frame = cap.read()
        if ret == False:
            break
        # frame consists of 1078 arrays. One for each height pixel.
        #      each array consists of 1360 arrays. One for each width pixel.
        #      each array consits of 3 values. RGB??
        return frame

def read_box(frame_no, nx1=0,nx2=2016,ny1=0,ny2=1600):
    # Open frame
    print("Start reading")
    cframe = open_frame(frame_no)
    pframe = open_frame(frame_no - 1)
    print("End reading")
    diff_frame = cframe[nx1:nx2, ny1:ny2] - pframe[nx1:nx2, ny1:ny2]
    return np.mean(diff_frame)

def process_job(args):
    start = args[0]
    end = args[1]
    name = args[2]
    if name not in waves:
        waves.update({name:[]})
    for frame in range(start, end):
        waves[name].append(read_box(frame))
    

