import time
from multiprocessing import Pool
import framer as f

procs = 6

def job(list_of_frames):
    a = []
    for frame in list_of_frames:
        a.append(f.read_box(frame))
    return a
 
def f_mp(list_of_frames):
    chunks = [list_of_frames[i::procs] for i in range(procs)]
    pool = Pool(processes=procs)
    result = pool.map(job, chunks)
    return result

list_of_frames = [i for i in range(24)]

if __name__ == "__main__":

    print("Testing times of two functions")
    print("Testing f")
    t1 = time.perf_counter()
    print(job(list_of_frames))
    t2 = time.perf_counter()
    print("Testing f_mp")
    t3 = time.perf_counter()
    g = f_mp(list_of_frames)
    t4 = time.perf_counter()
    print("Done")
    print("f took {} seconds.".format(t2-t1))
    print("f_mp took {} seconds.".format(t4-t3))
    print("Thats {} times quicker!".format((t2-t1)/(t4-t3)))