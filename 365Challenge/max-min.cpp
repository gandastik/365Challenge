#include<iostream>
/*find Max value of input and output to Max - Min*/
int main()
{
    int max = -2000000000;
    int min = 2000000000;
    int n;
    std::cin >> n;
    int arr[n];
    for(int i=0;i<n;i++)
    {
        std::cin >> arr[i];
    }
    for(int i=0;i<n;i++)
    {
        if(arr[i] > max)
        {
            max = arr[i];
        }
        if(arr[i] < min)
        {
            min = arr[i];
        }
    }
    std::cout << "max - min = " << max - min;
    return 0;
}