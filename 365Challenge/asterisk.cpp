/*Jan 14, 2021 -draw a star with odd input*/
#include<iostream>

int main()
{
    int n;
    std::cin >> n;
    for(int i=1;i<n+1;i++)
    {
        for(int j=1;j<n+1;j++)
        {
            if(i+j < n/2 +2)
                printf(" ");
            else if(j-i > n/2)
                printf(" ");
            else if(i-j > n/2)
                printf(" ");
            else if(i+j > n/2 + n+1)
                printf(" ");
            else printf("*");
        }
        printf("\n");
    }
    return 0;
}