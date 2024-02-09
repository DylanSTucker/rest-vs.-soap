#Dylan Tucker, dst833, 11235055
from multiprocessing import Process, Manager
import requests
import time
from matplotlib import pyplot as plt



def makeRequest(total_times, i):
    BASE = "http://127.0.0.1:5000/server/"

    for i in range(100):
        start = time.time()
        response = requests.post(BASE + "/" + str(5))
        end = time.time()
        total_times.append(end-start)

def run(total_times):
    proc = []
    for i in range(10):
        p = Process(target=makeRequest, args=(total_times, i))
        p.start()
        proc.append(p)
    for p in proc:
        p.join()

if __name__ == '__main__':
    t = Manager().list()
    run(total_times=t)
    mean = sum(t) / len(t)
    variance = sum([((x - mean) ** 2) for x in t]) / len(t) 

    print("average arrival time = " + str(mean))
    print("standard deviation = " + str(variance))

    print("longest arrival time = " + str(max(t)))
    print("shortest arrival time = " + str(min(t)))

    plt.plot(range(len(t)), t)
    plt.ylabel("time")
    plt.xlabel("number of requests")
    plt.show()
