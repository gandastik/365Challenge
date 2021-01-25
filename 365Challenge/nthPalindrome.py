#Jan 25, 2021 - find the nth palindrome number.
def nthPalindrome(num: int) -> int:
    ret = []
    n = 1
    while(len(ret) < num):
        reverse = 0
        temp = n
        while(temp > 0):
            r = temp % 10
            reverse = reverse * 10 + r
            temp = temp // 10
        if(n == reverse): ret.append(n)
        n += 1
    return ret[num-1]

n = int(input())
print(nthPalindrome(n))