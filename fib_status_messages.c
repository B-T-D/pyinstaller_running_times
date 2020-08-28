/* Status message helper functions related to C Fibonacci computation operations */

# include <stdio.h>
# include <string.h>

void
message_start(int n)
/* Handle English-language ordinal output for "computing nth Fib"--i.e. different suffixes
for 1st vs. 2nd vs. 3rd vs. 4th */
{

	char suffix[3]; // 3 character-array to hold the suffix
	
	/* Assign appropriate suffix based on last digit(s) */
	if (n % 10 == 1 && n % 100 != 11) // Special case n=11 should be "11th"
		strcpy(suffix, "st");
	else if (n % 10 == 2 && n % 100 != 12) // Special case n=12 should be "12th"
		strcpy(suffix, "nd");
	else if (n % 10 == 3)
		strcpy(suffix, "rd");
	else
		strcpy(suffix, "th");
	
	printf("Computing %d%s Fibonacci number\n", n, suffix);
}
