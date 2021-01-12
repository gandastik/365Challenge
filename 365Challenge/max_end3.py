#Jan 12, 2021 -given an array of integer length 3, figure out which is larger, the first element or last element in the array
#and set all the other elements to be that value, Return the changed array.
def max_end3(arr):
    ret = []
    if arr[2] > arr[0]:
        for i in range (3):
            ret.append(arr[2])
    else :
        for i in range(3):
            ret.append(arr[0])
    return ret
print(max_end3([3,11,3]))
