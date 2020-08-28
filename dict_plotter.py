"""Plot results dicts on a single pyplot."""

import matplotlib.pyplot as pyplot
from time_py_fib import time_py_fib
from dict_maker import txt_to_dict

def get_pure_python(n):
    """Run the python test and return the results dictionary."""
    return time_py_fib(n)
    

def get_pure_c(n):
    """Call dict_maker function on results of a previously run pure C time trial
    that were stored in a text file, and return that dict"""
    return txt_to_dict() # todo need to support an n arg

def plot(results1: dict, results2: dict=None, **kwargs):
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
    pyplot.plot(list(results1.keys()),
                list(results1.values()),
                label="Pure Python")
    if results2 is not None:
        pyplot.plot(list(results1.keys()),
                list(results1.values()),
                label="Pure C")
    pyplot.legend()
    pyplot.xlabel("nth Fibonacci Number")
    pyplot.ylabel("Running time (seconds)")
    pyplot.show()
                                            
    

def main():
    n = 20
    py_results = get_pure_python(n)
    plot(py_results)

if __name__ == '__main__':
    main()
    
