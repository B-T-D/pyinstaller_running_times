"""Empirical demonstration that Python subprocess module overhead is a constant
amount of time. When running a compiled C executable from a Python
script using the subprocess module to capture the stdout, the additional running
time imposed by the Python overhead is O(1) time complexity."""

import subprocess
import time
import argparse
import matplotlib.pyplot as pyplot

def time_c_fib(n):
    """Run C implementation fib(n) in subprocess and return its output. The
    C program's output is the running time."""
    # TODO take the name of the compiled C executable as an optional arg?

    command = "time_c_fib" # Base command that would be entered at command line
                            # to run the C executable
    start = time.time()
    completed_subproc = subprocess.run(f"{command} {n}", capture_output=True)
    result = float(completed_subproc.stdout)
    end = time.time()
    py_subprocess_time = end - start
    py_overhead = py_subprocess_time - result
    # Difference drops to trivial around n >= 45, observed on Windows 2020-08-28
    return (result, py_subprocess_time, py_overhead)
    
    
    # DB for curiosity, timing in python and compare with native C timing
    
def plot_overhead(data: dict):
    """Use pyplot to plot the results linearly with n on x axis, time on y axis."""
    xvals = list(data.keys())
    c_times = [data[n][0] for n in xvals]
    totals = [data[n][1] for n in xvals]
    overheads = [data[n][2] for n in xvals]
    pyplot.plot(xvals,
                c_times,
                label="C execution")
    pyplot.plot(xvals,
                totals,
                label="Total subprocess")
    pyplot.plot(xvals,
                overheads,
                label="Python subprocess overhead")
    pyplot.title("Python overhead for computing fib(n) with compiled C subprocess")
    pyplot.xlabel("n")
    pyplot.ylabel("Running time")
    pyplot.legend()
    #pyplot.savefig("Python overhead for C subprocess", format="png")
    pyplot.show()
    

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int,
                        nargs="?", # to make n optional
                        help="Which Fibonacci number to return,\
starting from fib(0) = 0")
    args = parser.parse_args()
    n = args.n
    if not n:
        print("No n argument")

    py_overhead_data = {}

    trials = [i for i in range(10, 41, 5)]
    for n in trials:
        output = time_c_fib(n)
        py_overhead_data[n] = output

    ## Output file init ##

    report_fobj = open("Python overhead for C subprocess.txt", mode='w')
    

    ## Output formatting ##
    label_n = 'n'
    colwidth_n = 4
    label_c = 'Native C time'
    colwidth_c = 2 + len(label_c)
    label_p = 'Python subprocess time'
    colwidth_p = 2 + len(label_p)
    label_s = 'Subprocess overhead'
    colwidth_s = 2 + len(label_s)
    
    header =\
           f"{label_n:^{colwidth_n}}|{label_c:^{colwidth_c}}|{label_p:^{colwidth_p}}|{label_s:^{colwidth_s}}"
    print(header)
    report_fobj.write(header + "\n")
    print('-' * len(header)) # horizontal row-separator under header row
    report_fobj.write('-' * len(header) + "\n")
    for n, results in py_overhead_data.items():
        print(f"\
{n:^{colwidth_n}}|\
{round(results[0], 6):^{colwidth_c}}|\
{round(results[1], 6):^{colwidth_p}}|\
{round(results[2], 6):^{colwidth_s}}")
        report_fobj.write(f"\
{n:^{colwidth_n}}|\
{round(results[0], 6):^{colwidth_c}}|\
{round(results[1], 6):^{colwidth_p}}|\
{round(results[2], 6):^{colwidth_s}}\n")

    report_fobj.close()

    plot_overhead(py_overhead_data)

if __name__ == '__main__':
    main()
