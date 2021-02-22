#51. Feb 20, 2021 - given N as a distance between your house to the school(in meters). 
# given that you can only walk 1,2,3,4,5 meters return the least step it takes you to arrive at school.
def howmanySteps(n: int) -> int:
    return n//5 + 1

n = int(input())
print(howmanySteps(n))