import time
import matplotlib.pyplot as pyplot
import json

import argparse
import sys

from fib import fib

def time_py_fib(n):
    """
    Time the execution of the pure Python Fibonacci function for input values
    [0, n-1] and return dictionary of the results, in format
    {(int) n: (float)seconds}
    """
    results = {}
    for i in range(n):
        start = time.time()
        fib(i)
        end = time.time()
        results[i] = end - start

    return results


def dump_results_to_json(results):
    # old spaghetti code, prob obviated
    filename = time.strftime("results pure python %Y-%m-%d %H%M") + '.json'
    with open(filename, 'w') as fobj:
        json.dump(results, fobj)
    fobj.close()

# pyplot
def placeholder_plot(): # old spaghetti code as placeholder for pyplot calls syntax
    pyplot.plot(list(times.keys()), list(times.values()),
                label="fib.py script runnning times for nth Fibonacci number")
    pyplot.legend()
    pyplot.xlabel("n")
    pyplot.ylabel("Seconds")
    pyplot.show()

def main():
    parser = argparse.ArgumentParser(description=\
                                     "Call recursive Fibonacci time-trial with\
##the n value provided at command line.")
    parser.add_argument('nth Fibonacci number', metavar='n', type=int, nargs='+',
                        help='Value of n for Fibonacci time trial')
    
    print(f"\nfull sys.argv list: {sys.argv}")
    args = parser.parse_args()
    n = int(sys.argv[1])
    time_py_fib(n)

if __name__ == '__main__':
    main()
