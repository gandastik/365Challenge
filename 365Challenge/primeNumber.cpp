#include<iostream>
/*input integer N find all of the prime number "between" 1 to N and how many of them*/
int main()
{
    int n, count = 0;
    bool check;
    std::cin >> n; //n >= 0 (positive integer)  
    for(int i=2;i<n;i++)
    {
        check = true;
        for(int j=2;j<i;j++)
        {
            if(i % j == 0)
            {
                check = false;
            }
        }
        if(check)
        {
            count++;
            std::cout << i << "\n";
        }
    }
    std::cout << "number of prime number(s) is " << count; 
    return 0;
}