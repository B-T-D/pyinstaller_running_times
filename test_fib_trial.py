import unittest

import fib_trial as ft

class TestBasicCoverage(unittest.TestCase):
    """Expedient simple-case tests to increase baseline coverage."""

    def setUp(self):
        n = 10
        self.trial = ft.FibTrial(n)

    def test_os_command_c_program_windows(self):
        n = self.trial.n # unpack local n just in case
        self.trial.os = "Windows"
        cprogram = "time_c_fib.exe"
        expected = f"time_c_fib {n}"
        actual = self.trial.os_command(cprogram)
        
        self.assertEqual(expected, actual)

    def test_os_command_py_program_windows(self):
        n = self.trial.n
        self.trial.os = "Windows"
        pyprogram = "time_py_fib.py"
        expected = f"python -m time_py_fib {n}"
        self.assertEqual(expected, self.trial.os_command(pyprogram))
        
        

if __name__ == '__main__':
    unittest.main()
