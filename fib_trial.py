import subprocess
import time
import argparse
import matplotlib.pyplot as pyplot
import platform
import sys

class FibTrial:
    """Object that runs a running-times experiment for various implementations of O(2^n) time
    recursive Fibonacci number function."""

    def __init__(self, n):
        self.n = n
        self.os = self.get_os()

    def get_os(self): # Wrapper so implementation can be swapped out
        """Wrapper utility to return the machine's operating system."""
        # Using platform.system() for readability (returns "Windows" instead of
        #   os.name which evaluates to "nt". Not sure what other considerations.
        if platform.system() == "Windows":
            return "Windows"
        elif platform.system() == "Linux":
            return "Linux"
        else:
            raise OSError("Couldn't identify operating system.")

    def os_command(self, program: str):
        """Return the OS-appropriate command to run executable."""
        # Check if it's a .py file or a compiled
        if program[-4:] == ".exe":
            program = program.strip(".exe")
            if self.os == "Windows":
                return f"{program} {self.n}"
            else:
                raise NotImplementedError
        elif program[-3:] == ".py": # Just let it loudly fail if e.g. pyw
            program = program.strip(".py")
            if self.os == "Windows":
                return f"python -m {program} {self.n}"
            else:
                raise NotImplementedError
        else:
            raise ValueError("Unrecognized fib-runner program file extension")

    def time_c(self): # doesn't need n as an arg because can access the attribute
        program = "time_c_fib.exe"
        if self.os == "Windows":
            command = "time_c_fib"
        elif self.os == "Linux":
            command = "./time_c_fib"

def time_c(n):
    """Run C implementation fib(n) in subprocess and return its output. The
    C program's output is the running time."""
    # TODO take the name of the compiled C executable as an optional arg?

    system = get_os() # Commandline syntax will depend on the OS
    if system == "Windows": 
        command = "time_c_fib"
    elif system == "Linux":
        command = "./time_c_fib"
    completed_subproc = subprocess.run(f"{command} {n}", capture_output=True)
    return float(completed_subproc.stdout)
        
def time_py(n):
    """Run pure Python implementation fib(n) in subprocess and return its output.
    The Python fib(n) module measures its running time internally and outputs it."""

    # TODO class attribute OS

    system = get_os() # Commandline syntax will depend on the OS
    if system == "Windows": 
        command = "python -m time_py_fib"
    elif system == "Linux":
        command = "python3 -m time_py_fib"
    completed_subproc = subprocess.run(f"{command} {n}", capture_output=True)
    return float(completed_subproc.stdout)

def time_pyi_onedir(n):
    """Run Pyinstaller one-directory build fib(n) implementation in subprocess and
    return its output (which is the running time)."""

    # TODO DRY
    
    system = get_os() # Commandline syntax will depend on the OS
    if system == "Windows": 
        command = r"dist\time_pyi_fib_win_od\time_pyi_fib_win_od"
    elif system == "Linux":
        command = "dist/time_pyi_fib_win_od/./time_pyi_fib_win_od" # TODO confirm this is right
    completed_subproc = subprocess.run(f"{command} {n}", capture_output=True)
    return float(completed_subproc.stdout)

def time_pyi_onefile(n):
    """Run Pyinstaller one-file build fib(n) implementation in subprocess and return its output
    (which is the running time)."""
    system = get_os() # Commandline syntax will depend on the OS
    if system == "Windows": 
        command = r"dist\time_pyi_fib_win_onefile"
    elif system == "Linux":
        command = "dist/./time_pyi_fib_win_onefile" # TODO confirm this is right
    completed_subproc = subprocess.run(f"{command} {n}", capture_output=True)
    return float(completed_subproc.stdout)
    
        
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

    results = {}
    trial_functions = {
        "C": time_c,
        "Python": time_py,
        "Pyinstaller onedirectory": time_pyi_onedir,
        "Pyinstaller onefile": time_pyi_onefile
        }

    for label, function in trial_functions.items():
        try:
            results[label] = function(n)
        except FileNotFoundError:
            print(f"Skipped {label} due to FileNotFoundError")

    for key in results.keys():
        print(f"{key}: {results[key]}")
    
if __name__ == '__main__':
    main()
