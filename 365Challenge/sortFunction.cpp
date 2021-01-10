/*Jan 10, 2021 -take input until the input is zero, and then take the string input, if the string input is Max 
then sort in descending order, if the string input is Min then sort in ascending order*/
#include<iostream>

int main()
{
    int arr[100], index = 0;
    while(1)
    {
        scanf("%d", &arr[index]);
        if(arr[index] == 0) break;
        index++;
    }
    std::string mode;
    std::cin >> mode;
    if(mode == "Max")
    {
        for(int i=0;i<index;i++)
        {
            for(int j=i+1;j<index;j++)
            {
                if(arr[i] < arr[j])
                {
                    int temp = arr[i];
                    arr[i] = arr[j];
                    arr[j] = temp;
                }
            }
        }
    }
    else if(mode == "Min")
    {
        for(int i=0;i<index;i++)
        {
            for(int j=i+1;j<index;j++)
            {
                if(arr[i] > arr[j])
                {
                    int temp = arr[i];
                    arr[i] = arr[j];
                    arr[j] = temp;
                }
            }
        }
    }
    for(int i=0;i<index;i++)
        printf("%d ", arr[i]);
    return 0;
}