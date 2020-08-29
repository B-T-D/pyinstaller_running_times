import unittest

import fib_trial as ft

class FibTrialBasicCoverage(unittest.TestCase):
    """Expedient simple-case tests to increase baseline coverage."""

    def setUp(self):
        n = 10
        self.trial = ft.FibTrial(n)
        self.c_name_win = "time_c_fib_win.exe"
        self.py_name = "time_py_fib.py"
        self.onedir_name_win = "time_pyi_fib_win_onedir.exe"
        self.onefile_name_win = "time_pyi_fib_win_onefile.exe"

        # TODO add Linux

    def test_is_pyi_name(self):
        # Should return true:
        self.assertTrue(self.trial._is_pyi_name(self.onedir_name_win))
        self.assertTrue(self.trial._is_pyi_name(self.onefile_name_win))

        # Should return false:
        self.assertFalse(self.trial._is_pyi_name(self.c_name_win))
        self.assertFalse(self.trial._is_pyi_name(self.py_name))

    def test_is_onedir_name(self):
        # Should return true:
        self.assertTrue(self.trial._is_onedir_name(self.onedir_name_win))

        # Should return false:
        self.assertFalse(self.trial._is_onedir_name(self.c_name_win))
        self.assertFalse(self.trial._is_onedir_name(self.py_name))
        self.assertFalse(self.trial._is_onedir_name(self.onefile_name_win))

    def test_is_onefile_name(self):
        # Should return true:
        self.assertTrue(self.trial._is_onefile_name(self.onefile_name_win))

        # Should return false:
        self.assertFalse(self.trial._is_onefile_name(self.c_name_win))
        self.assertFalse(self.trial._is_onefile_name(self.py_name))
        self.assertFalse(self.trial._is_onefile_name(self.onedir_name_win))

    def test_os_command_c_program_windows(self):
        n = self.trial.n # unpack local n just in case
        self.trial.os = "Windows"
        expected = f"{self.c_name_win.strip('.exe')} {n}"
        actual = self.trial.os_command(self.c_name_win)
        self.assertEqual(expected, actual)

    def test_os_command_py_program_windows(self):
        n = self.trial.n
        self.trial.os = "Windows"
        pyprogram = "time_py_fib.py"
        expected = f"python -m {self.py_name.strip('.py')} {self.trial.n}"
        self.assertEqual(expected, self.trial.os_command(self.py_name))

    def test_os_command_pyinstaller_onedir_windows(self):
        n = self.trial.n
        self.trial.os = "Windows"
        pyi_onedir_program = "time_pyi_fib_win_onedir.exe"
        expected = rf"dist\time_pyi_fib_win_onedir\time_pyi_fib_win_onedir {n}"
        self.assertEqual(expected,
                         self.trial.os_command(self.onedir_name_win))

    def test_os_command_pyinstaller_onefile_windows(self):
        n = self.trial.n
        self.trial.os = "Windows"
        pyi_onefile_program = "time_pyi_fib_win_onefile.exe"
        expected =\
                 rf"dist\{self.onefile_name_win[:-4]} {self.trial.n}"
        self.assertEqual(expected,
                         self.trial.os_command(self.onefile_name_win))

if __name__ == '__main__':
    unittest.main()
