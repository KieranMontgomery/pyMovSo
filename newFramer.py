import numpy as np
from mydia import Videos

video_path = "D:/Users\kmont\Documents\ExperimentalSound\ShadowGraph_Phoebus_Mach2.mp4"

def select_frames(total_frames, num_frames, fps, *args):
    """This function will return the indices of the frames to be captured"""
    N = 1
    t = np.arange(total_frames)
    f = np.arange(num_frames)
    mask = np.resize(f, total_frames)

    return t[mask < N][:num_frames].tolist()

# Let's assume that the duration of your video is 120 seconds
# and you want 1 frame for each second 
# (therefore, setting `num_frames` to 120)
reader = Videos(num_frames=18, mode=select_frames)

video = reader.read(video_path)  # A video tensor/array