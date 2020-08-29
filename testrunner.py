"""Run all of the project's unit tests."""
# py script instead of .bat for portability to Linux

import subprocess
import platform

def main():
    test_commands_win = [
        r"python -m test.test_fib_trial",
        r"python -m test.test_fib"
        ]

    results = {}

    if platform.system() == "Windows":
        commands = test_commands_win
    else:
        raise NotImplementedError
    
    for command in commands:
        print("\n -- NEW TEST PROCESS: --")
        print(f"subprocess: $ {command} ")
        completed_subproc = subprocess.run(f"{command}", capture_output=False)
        results[command] = completed_subproc.stdout
        
if __name__ == '__main__':
    main()
