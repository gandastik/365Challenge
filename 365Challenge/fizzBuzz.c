#include<stdio.h>
/*number between 1-100 output condition: Fizz when the number is the product of 3, Buzz when the number is the product of 5
,FizzBuzz when the number is the product of 3 and 5 and print the number is the number isn't match with any of the condition above*/
int main()
{
    for(int i=1;i<100;i++)
    {
        if(i % 3 == 0 && i % 5 == 0)
        {
            printf("FizzBuzz\n");
        }
        else if(i % 3 == 0)
        {
            printf("Fizz\n");
        }
        else if(i % 5 == 0)
        {
            printf("Buzz\n");
        }
        else printf("%d\n", i);
    }
    return 0;
}