def fib(n):
    """Recursively compute the nth Fibonacci number in O(2^n) time."""
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)
