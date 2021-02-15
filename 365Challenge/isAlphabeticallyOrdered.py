#46. Feb 15, 2021 - take in string as an input return true if the string is alphabetically in ordered else return false.
def isAlphabeticallyOrdered(s: str) -> bool:
    temp = s.lower()
    sorted_string = sorted(temp)
    s = "".join(sorted_string)
    return s == temp

s = str(input())
print(isAlphabeticallyOrdered(s))