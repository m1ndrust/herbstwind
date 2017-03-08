#include<stdlib.h>
#include<stdio.h>






int main (int argc, char **argv[])
{
	puts("Euler Three : Largest prime factor");
	puts("----------------------------------");
	/*
	In number theory, the prime factors of a positive integer are the prime numbers that divide that integer exactly.
	The prime factorization of a positive integer is a list of the integer's prime factors, together with their multiplicities; 
	the process of determining these factors is called integer factorization. 
	The fundamental theorem of arithmetic says that every positive integer has a single unique prime factorization
	*/
	int n = 607085147; // Not the same number as in project_euler(Number was too large)
	int i;
	int test = 100; 
	/*

		A Prime Number can be divided evenly only by 1 or itself.
		And it must be a whole number greater than 1. 

		Prime factorization of 100

		100 / 2 = 50	 OK Save 2
		50 / 2	= 25	 OK Save 2 
		25 / 2  = 12.5 	 !! NOT EVEN  increase 2 to 3
		25 / 3  = 8.333  !! NOT EVEN  increase 3 to 4
		25 / 4 = 6.25 	 !! NOT EVEN  increase 4 to 5
		25 / 5 = 5 		 OK Save 5
		5 / 5  = 1 		 OK Save 5 

		We get =  2 x 2 x 5 x 5 DONE! 

	*/
	printf("Getting prime factors from...->%d\n", test );

	for (i = 2; i < 11; ++i) // if i = 0, we divide by zero ;)
	{
		int new = test / i;

		//puts("----------------------------------");
		printf("After dividing 100 / %d\n", i );
		printf("This is new: [%d]\n", new );
		//puts("----------------------------------");
	}





}



