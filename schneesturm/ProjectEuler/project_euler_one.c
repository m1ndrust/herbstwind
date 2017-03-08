#include<stdio.h>
#include<stdlib.h>


int main (int argc, char **argv[])
{
	int end = 1001;
	int i;
	int sum = 0;
	puts("Projekt Euler One");
	puts("-----------------");

	//Multiplier of 3 or 5
	for (i = 0; i < end; ++i)
	{
		
		
		if ((i % 3 == 0) || (i % 5 == 0))
		{
			printf("%d ding\n",i );
			sum += i;
			printf("We are at sum %d\n",sum);
		}

	}

}