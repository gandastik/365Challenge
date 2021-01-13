/*Jan 13, 2021 -take integer as a input 'n' print out a stair case of a number 1-n with n lines*/
#include<iostream>

int main()
{
    int n;
    std::cin >> n;
    for(int i=1;i<n+1;i++)
    {
        for(int j=0;j<i;j++)
        {
            std::cout << i << " ";
        }
        if(i!=n)
            std::cout << "\n";
    }
    return 0;
}