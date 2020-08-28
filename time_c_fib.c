# include <stdio.h>
# include <time.h>
# include <stdlib.h>
# include <string.h>

# include "fib.c"

# define FILENAME_SIZE 19

void 
time_trial(int n, double *results_array)
/* Run trials for Fibonacci numbers from 0 to n-1 and return the results stored in array.*/
{
	int i;
	for (i=0; i<n; i++) {
		clock_t start = clock();
		fib(i);
		clock_t end = clock();
		results_array[i] = (( double )(end - start)) / CLOCKS_PER_SEC;
			/* Cast the quantity (end - start) to a double, otherwise too many 
			of the output values round to zero after dividing by CLOCKS_PER SEC,
			especially when CLOCKS_PER_SEC is 1 million */
	};
}

int main(int argc, char *argv[])
{
	int n = atoi(argv[1]);
	printf("Computing first %d Fibonacci numbers.\n", n);
	
	double *results = malloc(n * sizeof(results)); /* Initialize array of size n */
		/* Must be done dynamically with malloc, otherwise won't compile on Windows.
		GCC allows "double results[n]" without a constant value for n, but VS compiler
		doesn't.*/
	
	time_trial(n, results);	
	
	/* Write results to file */
	char filename[FILENAME_SIZE] = "results pure C.txt";
	/* file with stable name that Python script 
		knows */
	
	FILE *fp = fopen(filename, "w"); /* Behaving strangely on windows. Execution normal
		through last line immediately before this one. */
	
	int i;
	for (i=0; i < n; i++){
		//printf("%f\n", results[i]);
		fprintf(fp, "%d: %f\n", i, results[i]);
	};
	fclose(fp);
	
	return 0;	
}
