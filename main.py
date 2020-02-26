import logging
import threading
import time
import concurrent.futures
import framer as f


def thread_function(lims):
    start = lims[0]
    end = lims[1]
    end = start + 4
    name = lims[2]
    a = []
    logging.info("Thread {}: starting ({},{})".format(name, start, end))
    
    for i in range(start, end):
        a.append(f.read_box(i))
    logging.info("Thread %s: finishing", name)
    return a
    
threads = 6

r = f.num_of_frames//threads
job_ranges = [(i*r, (i+1)*r, i) for i in range(threads)] 

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    
    for r in job_ranges:
        print(thread_function(r))

    #with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        #executor.map(thread_function, job_ranges)