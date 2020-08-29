import subprocess
import argparse
import matplotlib.pyplot as pyplot
import platform

def get_os():
    """Wrapper utility to return the machine's operating system."""
    # Alternative: os.name, evaluates to "nt". Chose platform.system() for readability ("Windows")
    if platform.system() == "Windows": 
        return "Windows"
    elif platform.system() == "Linux":
        return "Linux"
    else:
        raise OSError("Couldn't identify operating system.")

class FibTrial: 
    """Object that runs a running-times experiment for various implementations of O(2^n) time
    recursive Fibonacci number function."""

     # TODO: return the actual fib values as well, as sanity check. Use a C program with a fast
        #   fib algorithm to validate the math.

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
        
        results = {}
        trial_functions = {
            "C": self.time_c,
            "Python": self.time_py,
            "Pyinstaller onedir": self.time_pyi_onedir,
            "Pyinstaller onefile": self.time_pyi_onefile
            }
        results = {}
        for label in trial_functions.keys():
            results[label] = [] # Values will be lists with one element per trial

        for trial in range(self.trials):
            print(f"running trial {trial} of {self.trials}", end="\r", flush=True) # progress counter
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
            print(f"\t{key}: {mean}")

        self.plot_bar(results)

    def plot_bar(self, results: dict) -> None:
        """Use pyplot to plot the mean running time of each implementation of fib(n)."""

        means = {}
        for key in results.keys():
            means[key] = sum(results[key]) / len(results[key])

        labels = list(results.keys())

        pyplot.bar(labels, list(means.values()), align='center', alpha=0.5)
        pyplot.title(f"Running times for {self.trials} trials of fib({self.n})")
        pyplot.xlabel("Implementation")
        pyplot.ylabel("Mean running time (seconds)")
        pyplot.tight_layout(pad=0.4)
        pyplot.show()

    def _is_pyi_name(self, program: str) -> bool: # maintainability in case file naming changes
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

    def os_command(self, program: str) -> str:
        """Return the OS-appropriate command to run executable."""
        # Check if .py file or a compiled
        if program[-4:] == ".exe":
            program = program[:-4] # using "strip('.exe' will think 'e' in 'onefile' is the
                                    # beginning of a new '.exe' instance and strip it.
            # Pyinstaller onedir vs. onefile will be in different directories by default     
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
        elif program[-3:] == ".py": # Fail loudly on a .pyw
            program = program[:-3]
            if self.os == "Windows":
                return f"python -m {program} {self.n}"
            else:
                raise NotImplementedError
        else:
            raise ValueError("Unrecognized fib-runner program file extension")

        raise ValueError(f"Couldn't generate OS command for program name {program}")

    def time_c(self):
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
