#include<iostream>
/*Jan 5, 2021 -Find average value of the inputs*/
int main()
{
    int n;
    float sum, avg;
    scanf("%d", &n);
    int arr[n];
    for(int i=0;i<n;i++)
    {
        scanf("%d", &arr[i]);
        sum += arr[i];
    }
    avg = sum / n;
    printf("Average = %.2f", avg);
    return 0;
}