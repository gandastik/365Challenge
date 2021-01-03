#include<iostream>
/*Bubble sort, input N as amount of number of input and sort in ascending order*/
int main()
{
    int n;
    std::cin >> n;
    int arr[n];
    for(int i=0;i<n;i++)
    {
        std::cin >> arr[i];
    }
    std::cout << "Before sort: ";
    for(int i=0;i<n;i++)
    {
        std::cout << arr[i] << " ";
    }
    for(int i=0;i<n;i++)
    {
        for(int j=i+1;j<n;j++)
        {
            if(arr[i] > arr[j])
            {
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }
    std::cout << "\nAfter sort: ";
    for(int i=0;i<n;i++)
    {
        std::cout << arr[i] << " ";
    }
    return 0;
}