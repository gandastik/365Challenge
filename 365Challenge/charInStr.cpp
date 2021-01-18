/*Jan 18, 2021 - find out howmany are the input char is in the string input*/
#include<iostream>

int len(char str[])
{
    char* ptr = str;
    int count = 0;
    while(*ptr != '\0')
    {
        count++;
        ptr++;
    }
    return count;
}

int main()
{
    char strA[100], strB[50];
    std::cin >> strA >> strB;
    int counter = 0;
    for(int i=0;i<len(strA);i++)
    {
        for(int j=0;j<len(strB);j++)
        {
            if(strA[i] == strB[j])
                counter++;
        }
    }
    std::cout << counter;
    return 0;
}