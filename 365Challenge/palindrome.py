#Jan 18, 2021 - write a function that take string and determine if the string is palindrom or not.
def palindrome(string: str) -> bool:
    idx1 = 0
    idx2 = len(string) - 1
    for i in range(int(len(string))):
        if(string[idx1] != string[idx2]):
            return False
        idx1+=1
        idx2-=1
    return True

string = str(input())
if(palindrome(string)):
    print("Palindrome")
else: print("Not Palindrom")