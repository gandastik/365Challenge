#Jan 9, 2021 - decode the string input backward
string = input().split()
for i in range(len(string) - 1, -1, -1):
    print(string[i], end=" ")