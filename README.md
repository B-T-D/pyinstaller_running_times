# Pyinstaller running times experiment
Comparison of running times for four different implementations of a CPU-intensive exponential-time algorithm for computing the nth number in the Fibonacci sequence:
1. Compiled C program
2. Python program running in CPython interpreter
3. Python program bundled into a Pyinstaller executable using single-folder approach
4. Python program bundled into Pyinstaller executable using single-executable approach

# Background
I became casually familiar with pyinstaller when I used it to bundle some Python scripts here and there. In [the pyinstaller documentation](https://pyinstaller.readthedocs.io/en/stable/), I read about the difference between one-folder bundling and one-file bundling, and became curious whether running times would be different based on the bundling method. So I decided to try running an identical, deliberately slow program in different pyinstaller configurations, and measure its running time.

For the slow program, I used a recursive algorithm that computes Fibonacci numbers in exponential time complexity. As a control and sanity check against the bundled pyinstaller programs, I also timed the same algorithm implemented in a compiled C program.

Along the way, I noticed I could also measure the computational overhead involved in using a Python subprocess to run a C program. So out of curiosity, I timed that too.

# Results
* Observed no significant or even consistent running time difference between the three Python-based implementations of the algorithm
* C implementation consistently ran at least 50 times faster than any of the three Python implementations
* Overhead imposed by using Python subprocess module to run a C process from a parent Python script is a constant factor that becomes insignificant with computationally large inputs.

## Running time by implementation
![n30t100](/results_data/means_n30_trials1000.png)

  See [fib_trial.py](fib_trial.py)

## Python overhead for C subprocess
![Python overhead](/results_data/python_overhead_for_c_subprocess.png)

  See [c_subprocess_overhead_demo.py](c_subprocess_overhead_demo.py)

# How to run the experiment

## Building executables
  The experiment-runner expects specific file names for the executables, and won't work if they don't match. 
### Compiling C program

#### Windows
Visual studio developer command prompt:

    $ cd <project_directory>/c_files
    $ cl time_c_fib.c /link /out:time_c_fib_win.exe

### Bundling Pyinstaller executables

#### Windows
Use the batchfile scripts:

    $ build_onedir
    $ build_onefile

## Running experiment-runner script
  Experiment runner script, fib_trial.py, requires two command-line arguments: the value of n for which Fibonacci number to compute, and the number of trials over which to repeat the computation:
    
    usage: fib_trial.py [-h] [n] [trials]

    positional arguments:
      n           Which Fibonacci number to return, starting from fib(0) = 0
      trials      Number of times to repeat computation of fib(n)

    optional arguments:
      -h, --help  show this help message and exit
  
  
