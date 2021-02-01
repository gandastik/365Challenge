#Feb 1, 2021 - write a program that take input, the first input begin the target number,
#take number input until zero found, output the amount of the consecutive appearence of the target number 
#and the amount of the appearence of the target number.
nums = []
i = 0
consec = 0
count = 0
cnt = 0
n = int(input())
while(True):
    x = int(input())
    nums.append(x)
    if(nums[i] == 0):
        break
    if(nums[i] == n):
        count += 1
        cnt += 1
    else:
        count = 0
    i += 1
    if(count > consec):
        consec = count

print(consec)
print(cnt)