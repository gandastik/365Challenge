#include<iostream>
/*encoding method :caesar cipher shifted by one*/
int main()
{
    int i = 0;
    char arr[10];
    std::cin >> arr;
    while(arr[i] != '\0')
    {
        if(arr[i] == 'z') arr[i] = 'a';
        else arr[i] += 1;
        i++;
    }
    printf("%s", arr);
    return 0;
}