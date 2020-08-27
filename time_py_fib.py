import time
import matplotlib.pyplot as pyplot

from fib import fib


times = {} # {n: time}

n = 35
for i in range(n):
    print(f"computing Fibonacci number {i} of {n}", end="\r", flush=True)
    start = time.time()
    fib(i)
    end = time.time()
    elapsed = end - start
    times[i] = elapsed

print("\n-------RESULTS-------")

for key, value in times.items():
    print(f"{key}: {value}")


# pyplot
pyplot.plot(list(times.keys()), list(times.values()),
            label="fib.py script runnning times for nth Fibonacci number")
pyplot.legend()
pyplot.xlabel("n")
pyplot.ylabel("Seconds")
pyplot.show()
