#42. Feb 11, 2021 - take input as a string and then output how many of each individually character.
def howManyChar(s: str) -> dict:
    s = s.lower()
    dic = dict()
    for i in range(len(s)):
        dic[s[i]] = 0
        for j in range(len(s)):
            if(s[i] == s[j]):
                dic[s[i]] += 1            
    return dic 

s = str(input())
dic = howManyChar(s)
for i in dic.keys():
    print("%s = %d" %(i , dic[i]))
