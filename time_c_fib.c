# include <stdio.h>
# include <time.h>
# include <stdlib.h>

# include "fib.c"

# define TIMESTAMP_SIZE 17
# define FILENAME_SIZE 34

int main(int argc, char *argv[])
{
	int n = atoi(argv[1]);
	printf("Computing first %d Fibonacci numbers.\n", n);
	double results[n]; /* Array of size n to store results */
	int i;
	clock_t processor_start = clock();
	
	for (i = 0; i < n; i++) {
		clock_t start = clock();
		//time_t start;
		//time(&start);
		fib(i);
		clock_t end = clock();
		//time_t
		//time(&end);
		results[i] = (end - start) / CLOCKS_PER_SEC;
	};
	
	clock_t processor_end = clock();
	printf("processor_end - processor_start = %ld clock cycles\n",
	processor_end - processor_start);
	printf("CLOCKS_PER_SEC constant defined as %ld\n", CLOCKS_PER_SEC);
	long total_seconds = (processor_end - processor_start) / CLOCKS_PER_SEC; 
		/* CLOCKS_PER_SEC constant is already #define d in <time.h> */
	printf("total seconds = clocks / CLOCKS_PER_SEC = %ld\n", total_seconds);
	
	char filename[FILENAME_SIZE];
	time_t stamp; /* timestamp for use in results filename */
	struct tm *pointer_to_stamp;
	stamp = time(NULL);
	//time(&stamp);
	//printf("%s\n", ctime(&stamp));
	size_t smax = 15; /* max of 15 characters for the filename timestamp */
	char stampstring[TIMESTAMP_SIZE];
	strftime(filename, sizeof(stampstring), "%Y-%m-%d %H%M", localtime(&stamp));
	printf("%s\n", filename);
	
	
	FILE *fp = fopen(filename, "w");
	for (i=0; i < n; i++){
		printf("%f\n", results[i]);
		//fgets(i);
		fprintf(fp, "%d: %f\n", i, results[i]);
		//fprintf(fp, "\n");
	};
	fclose(fp);
	return 0;	
}
