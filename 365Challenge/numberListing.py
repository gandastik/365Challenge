#37. Feb 6, 2021 - sorting the list input in ascending order.
nums = [int(x) for x in input().split()]
for i in range(len(nums)):
    for j in range(len(nums)):
        if(nums[i] < nums[j]):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

for i in nums:
    print("%d " % i, end="")