#Dylan Tucker, dst833, 11235055
from suds.client import Client
import time
import sys

sys.set_int_max_str_digits(0)


total_times = []



for i in range(100):
    start = time.time()
    hello_client = Client('http://localhost:8000/?wsdl')
    hello_client.service.fib(5)
    end = time.time()
    total_times.append(end-start)
    #print("this request took " + str(end-start) + " seconds")
    #print("-"*80)


from matplotlib import pyplot as plt

mean = sum(total_times) / len(total_times)
variance = sum([((x - mean) ** 2) for x in total_times]) / len(total_times) 

print("average arrival time = " + str(mean))
print("standard deviation = " + str(variance))
print("longest arrival time = " + str(max(total_times)))
print("shortest arrival time = " + str(min(total_times)))

plt.plot(range(len(total_times)), total_times)
plt.ylabel("time")
plt.xlabel("number of requests")
plt.show()