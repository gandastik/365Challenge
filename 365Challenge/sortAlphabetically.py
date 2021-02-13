#44. Feb 13, 2021 - take string as input sort it alphabetically from Upper case to Lower case
def sortAlphabetically(s: str) -> str:
    lst = []
    for i in s:
        lst.append(ord(i))
    lst.sort()
    ret = ''
    for i in lst:
        ret+=chr(i)
    return ret

s = str(input())
print(sortAlphabetically(s))