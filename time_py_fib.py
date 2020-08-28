import time
import json

import argparse
import sys

from fib import fib

def in_pyinstaller():
    """Return True if running in PyInstaller bundle."""
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        return True

def time_py_fib(n):
    """
    Time the execution of the pure Python Fibonacci function for input values
    [0, n-1] and return dictionary of the results, in format
    {(int) n: (float)seconds}
    """
    results = {} # This should have trivially lower constant factor than the C implementation,
                #   because C writes its results to an array with O(n) insertion, while
                # this is writing to a hash map with O(1) insertion. 
    for i in range(n):
        start = time.time()
        fib(i)
        end = time.time()
        results[i] = end - start

    return results

def save_results_to_txt(results: dict):
    """
    Save the results to a txt file formatted the same way as the C implementation's output,
    such that can be parsed into a dict on another system by the same Python function as
    converts C's txt output.
    """
    # todo class attribute n would be useful here--assert len matches n
    if in_pyinstaller():
        filename = "results pyinstaller python.txt"
    else:
        filename = "results pure python.txt"
    fobj = open(filename, mode='w')
    for key, value in results.items():
        fobj.write(f"{key}: {value}\n")
    fobj.close()
        
def dump_results_to_json(results):
    # old spaghetti code, prob obviated
    filename = time.strftime("results pure python %Y-%m-%d %H%M") + '.json'
    with open(filename, 'w') as fobj:
        json.dump(results, fobj)
    fobj.close()

def main():
    parser = argparse.ArgumentParser(description=\
                                     "Call recursive Fibonacci time-trial with\
the n value provided at command line.")
    parser.add_argument('nth Fibonacci number', metavar='n', type=int, nargs='+',
                        help='Value of n for Fibonacci time trial')
    
    args = parser.parse_args()
    n = int(sys.argv[1])
    results = time_py_fib(n)
    save_results_to_txt(results)

if __name__ == '__main__':
    main()
