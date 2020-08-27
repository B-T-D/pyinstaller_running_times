import time
import matplotlib.pyplot as pyplot
import json

from fib import fib


times = {} # {n: time}

n = 30
for i in range(n):
    start = time.time()
    fib(i)
    end = time.time()
    elapsed = end - start
    times[i] = elapsed

print("\n-------RESULTS-------")

for key, value in times.items():
    print(f"{key}: {value}")

filename = time.strftime("results pure python %Y-%m-%d %H%M") + '.json'
with open(filename, 'w') as fobj:
    json.dump(times, fobj)
fobj.close()

# pyplot
pyplot.plot(list(times.keys()), list(times.values()),
            label="fib.py script runnning times for nth Fibonacci number")
pyplot.legend()
pyplot.xlabel("n")
pyplot.ylabel("Seconds")
pyplot.show()
