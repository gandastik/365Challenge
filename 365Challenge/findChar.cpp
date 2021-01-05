#include<iostream>
/*Jan 5, 2021 -find how many are the ";" in the input string*/
int main()
{
    char arr[100];
    int i = 0, counter = 0;
    scanf("%[^\n]", arr);
    while(arr[i] != '\0')
    {
        if(arr[i] == ';')
        {
            counter++;
        }
        i++;
    }
    std::cout << "counter = " << counter;
    return 0;
}