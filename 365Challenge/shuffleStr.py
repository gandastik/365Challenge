#Jan 20, 2021 - shuffle a string input with the list of indices
from typing import List
def shuffleStr(s: str, indices: List[int]) -> str :
    temp = dict()
    ret = ""
    for i in range(len(s)):
        temp[indices[i]] = s[i]
    dic = sorted(temp.keys())
    for i in range(len(s)):
        ret += (temp[i])
    return ret

print(shuffleStr("aaiougrt", [4,0,2,6,7,3,1,5]))