# Pyinstaller running times experiment
Comparison of running times for four different implementations of a CPU-intensive exponential-time algorithm for computing the nth number in the Fibonacci sequence:
1. Compiled C program
2. Python program running in CPython interpreter
3. Python program bundled into a Pyinstaller executable using single-folder approach
4. Python program bundled into Pyinstaller executable using single-executable approach

## Results
* Observed no significant or even consistent running time difference between the three Python-based implementations of the algorithm
* C implementation consistently ran at least 50 times faster than any of the three Python implementations
* Overhead imposed by using Python subprocess module to run a C process from a parent Python script is a constant factor that becomes insignificant with computationally large inputs.

# Running the experiment

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
  
  
