#include<iostream>
/*Bubble sort, Descending order*/
int main()
{
    int n;
    std::cin >> n;
    int arr[n];
    for(int i=0;i<n;i++)
    {
        std::cin >> arr[i];
    }
    for(int i=0;i<n;i++)
    {
        for(int j=i+1;j<n;j++)
        {
            if(arr[i] < arr[j])
            {
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }
    std::cout << "\nAfter sort" << std::endl;
    for(int i=0;i<n;i++)
    {
        std::cout << arr[i] << std::endl;
    }
    return 0;
}