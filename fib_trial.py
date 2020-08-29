import subprocess
import time
import argparse
import matplotlib.pyplot as pyplot
import platform
import sys

def get_os(): # Outside class for expediency, so __init__ can call it the one and only time
    """Wrapper utility to return the machine's operating system."""
    # Using platform.system() for readability (returns "Windows" instead of
    #   os.name which evaluates to "nt". Not sure what other considerations.
    if platform.system() == "Windows":
        return "Windows"
    elif platform.system() == "Linux":
        return "Linux"
    else:
        raise OSError("Couldn't identify operating system.")

class FibTrial:

    # TODO: Need to take a mean of the execution times. All three python ones jump around at
    #   n=40 enough that there's not a consistent rank ordering.

        # Try 10 trials at n=35. Python should run in under 3 seconds for n=35, on desktop's
        # hardware.

    # TODO: That needs multicore processing--that will cut the total running time of each trial
    #   to almost 1/3rd (if they all ran at once, and C is rounded to zero).

    # TODO: return the actual fib values as well, as sanity check. Use a C program with a fast
    #   fib algorithm to validate the math.
    
    """Object that runs a running-times experiment for various implementations of O(2^n) time
    recursive Fibonacci number function."""

    def __init__(self, n, trials):
        self.n = n
        self.trials = trials
        self.os = get_os()
        self.c_name_win = "time_c_fib_win.exe"
        self.py_name = "time_py_fib.py"
        self.onedir_name_win = "time_pyi_fib_win_onedir.exe"
        self.onefile_name_win = "time_pyi_fib_win_onefile.exe"

    def run(self):
        """Run the trial and output to stdout and files as appropriate."""
        # TODO validate useability of the trial executables
        
        results = {}
        trial_functions = {
            "C": self.time_c,
            "Python": self.time_py,
            "Pyinstaller onedirectory": self.time_pyi_onedir,
            "Pyinstaller onefile": self.time_pyi_onefile
            }
        results = {}
        for label in trial_functions.keys():
            results[label] = [] # Values will be lists with one element per trial

        for trial in range(self.trials):
            print(f"running trial {trial} of {self.trials}", end="\r", flush=True)
            for label, function in trial_functions.items():
                try:
                    results[label].append(function()) # The functions get n from the class attribute
                except FileNotFoundError:
                    print(f"Skipped {label} due to FileNotFoundError")
        print(" " * 50, end="\r") # Blank out the line in case next print is shorter
        print(f"Completed {self.trials} trials")
        
        print(f"Mean running times:")
        for key in results.keys():
            mean = sum(results[key]) / len(results[key])
            print(f"{key}: {mean}")

        print(f"Full results:")
        for key in results.keys():
            print(f"{key}: {results[key]}")

        self.plot_bar(results)

    def plot_bar(self, results: dict):
        """Use pyplot to plot the mean running time of each implementation of fib(n)."""

        means = {}
        for key in results.keys():
            means[key] = sum(results[key]) / len(results[key])

        labels = list(results.keys())

        pyplot.bar(labels, list(means.values()), align='center', alpha=0.5)
        pyplot.title(f"Running times for {self.trials} trials of fib({self.n})")
        pyplot.xlabel("Implementation")
        pyplot.ylabel("Mean running time (seconds)")
        pyplot.show()
        
        

    def _is_pyi_name(self, program: str) -> bool: # For ease of maintenance if naming convention changes
        """Return True if string is indicative of the naming convention for one of the project's
        pyinstaller executables, else False."""
        
        return "pyi" in program

    def _is_onedir_name(self, program: str) -> bool:
        """Return True if program follows project's naming convention for pyinstaller --onedir
        build executables, else False."""

        return "onedir" in program

    def _is_onefile_name(self, program: str) -> bool:
        """Return True if program follows project's naming convention for pyinstaller --onefile
        build executables, else False."""

        return "onefile" in program

    def os_command(self, program: str):
        """Return the OS-appropriate command to run executable."""
        # Check if it's a .py file or a compiled
        if program[-4:] == ".exe":
            program = program[:-4] # using "strip('.exe' will think 'e' in 'onefile' is the
                                    # beginning of a new '.exe' instance and strip it.
            # check if it's a pyinstaller exe that would be in a different directory       
            if self._is_pyi_name(program): # Then check onedir vs. onefile naming convention
                if  self._is_onedir_name(program):
                    if self.os == "Windows":
                        return rf"dist\{program}\{program} {self.n}"
                    elif self.os == "Linux":
                        raise NotImplementedError
                elif self._is_onefile_name(program):
                    if self.os == "Windows":
                        return rf"dist\{program} {self.n}"
                    elif self.os == "Linux":
                        raise NotImplementedError
            else: # Then it should be a C executable      
                if self.os == "Windows":
                    return rf"{program} {self.n}"
                else:
                    raise NotImplementedError
        elif program[-3:] == ".py": # Just let it loudly fail if e.g. pyw
            program = program[:-3]
            if self.os == "Windows":
                return f"python -m {program} {self.n}"
            else:
                raise NotImplementedError
        else:
            raise ValueError("Unrecognized fib-runner program file extension")

        print(f"******  program = {program}  ******")
        raise Exception ("shouldn't have gotten here without returning") # TODO DB

    def time_c(self): # doesn't need n as an arg because can access the attribute
        command = self.os_command(self.c_name_win)
        completed_subproc = subprocess.run(f"{command}", capture_output=True)
        return float(completed_subproc.stdout)

    def time_py(self):
        command = self.os_command(self.py_name)
        completed_subproc = subprocess.run(f"{command}", capture_output=True)
        return float(completed_subproc.stdout)

    def time_pyi_onedir(self):
        command = self.os_command(self.onedir_name_win)
        completed_subproc = subprocess.run(f"{command}", capture_output=True)
        return float(completed_subproc.stdout)

    def time_pyi_onefile(self):
        command = self.os_command(self.onedir_name_win)
        completed_subproc = subprocess.run(f"{command}", capture_output=True)
        return float(completed_subproc.stdout)
        
def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int,
                        nargs="?",
                        help="Which Fibonacci number to return,\
starting from fib(0) = 0")
    parser.add_argument("trials",
                        type=int,
                        nargs="?",
                        help="Number of times to repeat computation \
of fib(n)")
                        
    args = parser.parse_args()
    n = args.n
    trials=args.trials
    if not n:
        print("No n argument")

    trial = FibTrial(n, trials)
    trial.run()

if __name__ == '__main__':
    main()
