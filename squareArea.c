#include<stdio.h>
/*find the area of the square and get the 2 decimal output*/
int main()
{
    float height, width, area;
    scanf("%f %f", &height, &width);
    area = height * width;
    printf("%.2f", area);
    return 0;
}