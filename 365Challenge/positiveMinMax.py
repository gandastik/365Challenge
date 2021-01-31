#Jan 31, 2021 - find the min and the max of the positive number of 8 inputs.
nums = []
min = 20000000000000
max = -20000000000000
for i in range(8):
    nums.append(int(input()))
    if(nums[i] > 0):
        if(nums[i] > max):
            max = nums[i]
        if(nums[i] < min):
            min = nums[i]

print(max)
print(min)