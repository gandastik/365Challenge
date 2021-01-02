#include<iostream>
/*recursive function pratice!, When x > 0 f(x) = f(x-1) + 100, f(0) = 1, f(x) when x < 0 = -1*/

void fx(int n, int* counter)
{
    if(n >0)
    {
        fx(n-1, counter);
        *counter += 100;
    }
    else if(n == 0)
    {
        *counter += 1;
    }
    else 
    {
        *counter = -1;
    }
}

int main()
{
    int n, counter;
    counter = 0;
    int* ptr = &counter;
    std::cin >> n;
    fx(n, ptr);
    std::cout << *ptr << std::endl;
    return 0;
}

