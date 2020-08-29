# pyinstaller_running_times
Running times experiment for Pyinstaller executables

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
