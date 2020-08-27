# include <stdio.h>
# include <time.h>
# include <stdlib.h>

# include "fib.c"

int main(int argc, char *argv[])
{
	int n = atoi(argv[1]);
	printf("Computing first %d Fibonacci numbers.\n", n);
	int i;
	//time_t start;
	//time(&start);
	for (i = 0; i < n; i++)
		printf("%lu\n", fib(i));
	//time_t end;
	//time(&end);
	//printf("%s\n", ctime(&start));
	//printf("%s\n", ctime(&end));
	return 0;	
}
