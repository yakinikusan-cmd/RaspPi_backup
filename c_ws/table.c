#include <stdio.h>
int main(void)
{
	int person1,person2,person3;
	float mark1,mark2,mark3;
	person1 = 5;
	person2 = 48;
	person3 = 145;
	mark1 =  86.5;
	mark2 = 78.2;
	mark3 = 9.6;
	printf("%4d番%6.1f点\n%4d番%6.1f点\n%4d番%6.1f点\n",person1,mark1,person2,mark2,person3,mark3);
	return 0;
}
