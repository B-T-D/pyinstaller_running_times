unsigned long fib(int n)
/* fib: Return the nth Fibonacci number using recursive exponential time algorithm */
{
	if (n == 0)
		return 0;
	if (n == 1)
		return 1;
	return fib(n - 1) + fib(n - 2);
}
