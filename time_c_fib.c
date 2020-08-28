/*Compute fib(n) for command line arg value of n, and return computation time in seconds
(don't return the fib value itself)*/

# include <stdio.h>
# include <time.h>
# include <stdlib.h>
# include <string.h>

# include "fib.c"
# include "fib_status_messages.c"

int main(int argc, char *argv[])
{
	int n = atoi(argv[1]);
	
	double result;
	clock_t start = clock();
	fib(n);
	clock_t end = clock();
	result = ( double )(end - start) / CLOCKS_PER_SEC; /* Cast numerator to double to avoid
		rounding to zero for small n values */
	
	printf("%f", result); /* Output only the result value in its original type */
	
	return 0;	
}
