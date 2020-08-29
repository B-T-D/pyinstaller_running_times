import unittest

import fib

class TestFib(unittest.TestCase):

    def test_base_case_0(self):
        """The first Fibonacci number (n=0) is zero."""
        n = 0
        self.assertEqual(0, fib.fib(n))

    def test_base_case_1(self):
        """The next Fibonacci number (n=1) is 1."""
        n = 1
        self.assertEqual(1, fib.fib(n))

    def test_first_6(self):
        """The first six Fibonacci numbers are 0, 1, 1, 2, 3, 5."""
        expected = [0, 1, 1, 2, 3, 5]
        for i in range(6):
            self.assertEqual(expected[i], fib.fib(i))

if __name__ == '__main__':
    unittest.main()
    
