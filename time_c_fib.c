# include <stdio.h>
# include <time.h>
# include <stdlib.h>
# include <string.h>

# include "fib.c"

# define TIMESTAMP_SIZE 17
# define STAMPED_FILENAME_SIZE 34
# define FILENAME_SIZE 19

void timestamp_filename(char *filename)
/* Return string for use as differentiable filename, based on the current time. */
{
		//char filename[STAMPED_FILENAME_SIZE];
		printf("filename: %s\n", filename);
		time_t stamp; /* Create timestamp string */
		printf("ok\n");
		struct tm *pointer_to_stamp;
		printf("still ok\n");
		stamp = time(NULL);
		size_t smax = 15; /* Max of 15 characters needed for the timestamp part of the filename,
		'YYYY-MM-DD HHMM" */
		char stampstring[TIMESTAMP_SIZE];
		strftime(filename, sizeof(stampstring), "%Y-%m-%d %H%M", localtime(&stamp));
		printf("filename: %s\n", filename);
		strcat(filename, " results pure C.txt");
		return filename;
}

int main(int argc, char *argv[])
{
	int n = atoi(argv[1]);
	printf("Computing first %d Fibonacci numbers.\n", n);
	double *results = malloc(n * sizeof(results)); /* Must be done dynamically with malloc, 
	else it won't compile on Windows. GCC lets you use double my_array_of_doubles[n] for a 
	dynamically changeable value of n, but VS compiler doesn't. */
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
	
	/* Create differentiable filename based on current time */
	//char filename[FILENAME_SIZE];
	//time_t stamp; /* timestamp for use in results filename */
	//struct tm *pointer_to_stamp;
	//stamp = time(NULL);
	//size_t smax = 15; /* max of 15 characters for the filename timestamp */
	//char stampstring[TIMESTAMP_SIZE];
	//strftime(filename, sizeof(stampstring), "%Y-%m-%d %H%M", localtime(&stamp));
	
	//strcat(filename, " results pure C.txt");
	
	//char tstamp_fname[STAMPED_FILENAME_SIZE];
	//timestamp_filename(tstamp_fname);
	
	//printf("%s\n", tstamp_fname);
	
	/* Write results array to individualized file */
	char filename[FILENAME_SIZE];
	strcat(filename, "results pure C.txt");
	FILE *fp = fopen(filename, "w");
	for (i=0; i < n; i++){
		printf("%f\n", results[i]);
		//fgets(i);
		fprintf(fp, "%d: %f\n", i, results[i]);
		//fprintf(fp, "\n");
	};
	fclose(fp);
	
	/* Overwrite the "latest" file with the new results--the file whose
	name the Python dict converter knows. */
	
	
	return 0;	
}
