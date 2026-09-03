from collections import Counter
def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    set1 = []
    set2 = []

    for i in range(len(str1)-1):
        s = str1[i:i+2]
        if s.isascii() and s.isalpha():
            set1.append(s)
    for i in range(len(str2)-1):
        s = str2[i:i+2]
        if s.isascii() and s.isalpha():
            set2.append(s)
            
    count1 = Counter(set1)
    count2 = Counter(set2)
    
    union = count1|count2
    inter = count1&count2
    
    union_count = sum(union.values())
    inter_count = sum(inter.values())
    
    if len(union) == 0:
        return 65536

    return int(inter_count/union_count*65536)

## 풀이전략, 핵심 아이디어
# 문자열을 두 글자씩 자른다 -> 영어 문자로만 된 것만 남긴다 -> Counter로 개수를 센다 -> 교집합과 합집합을 구한다 -> 전체 개수를 구하고 return
