"""Plot results dicts on a single pyplot."""

import matplotlib.pyplot as pyplot

import matplotlib
#matplotlib.use('GTK3Agg')
from time_py_fib import time_py_fib
from dict_maker import txt_to_dict

def get_pure_python(n):
    """Run the python test and return the results dictionary."""
    return time_py_fib(n)
    

def get_pure_c(n):
    """Call dict_maker function on results of a previously run pure C time trial
    that were stored in a text file, and return that dict"""
    return txt_to_dict(filename="results pure C.txt") # todo need to support an n arg

def plot_line(results1: dict, results2: dict=None, **kwargs):
##    print(locals())
##    print(f"locals() is type...")
##    print(type(locals()))
##    for var in locals().values():
##        print(type(var))
##        if type(var) == dict:
##            print(f"localvar {var} is a dict")
##
##    for name in locals().keys():
##        print(f"name.value(): {name.value()}")
    xvals = list(results1.keys()) # todo class instance variable self.n would be useful here
    pyplot.plot(xvals,
                list(results1.values()),
                label="results1")
    if results2 is not None:
        pyplot.plot(xvals,
                list(results2.values()),
                label="Pure C")
    pyplot.legend()
    pyplot.xlabel("nth Fibonacci Number")
    pyplot.ylabel("Running time (seconds)")
    pyplot.show()

def plot_bar(results1, results2=None, **kwargs):
    """Plot the running time for fib(n) as a bar. Only fib(n), not all fib(i) for i 
    in range (0, n)"""
    results = {} # format {(str) implementation: (float) seconds}
    results["Python"] = max(results1.values())
    results["C"] = max(results2.values())
    
    print(results)
    
    pyplot.bar(list(results.keys()), list(results.values()), align='center', alpha=0.5)
    pyplot.xlabel("Implementation")
    pyplot.ylabel("Running time (seconds)")
    pyplot.show()                                  
    

def main():
    n = 40
    py_results = get_pure_python(n)
    c_results = get_pure_c(n)
    #plot_line(c_results)
    plot_bar(py_results, c_results)

if __name__ == '__main__':
    main()
    
