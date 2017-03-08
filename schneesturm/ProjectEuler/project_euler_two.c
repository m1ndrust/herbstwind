#include<stdio.h>
#include<stdlib.h>


int fibo(int n)
	{
		if (n <= 1)
		{
			return n;
		}
		else
		{
		  return fibo(n-1) + fibo(n-2); 
		}

	}





int main (int argc, char **argv[])
{
	//int bound = 100;
	int n;
	puts("Euler Two : Even fibonacci numbers");
	puts("----------------------------------");
	//Solved with recursion(The fibo function calls itself)

	for (n = 1; n < 100; ++n) // 
	{
		printf("%d\n",fibo(n));

			if (fibo(n) > 4000000  )
			{
				puts("Upper limit reached.");
				exit(0);
			}
			else if(fibo(n) % 2 == 0 )
			{
				puts("Caught even number");
			}
	}

	


	





}