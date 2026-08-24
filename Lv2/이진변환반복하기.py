def solution(s):
    count = 0
    zero = 0
    
    while s != "1":
        zero += s.count("0")
        s = s.replace("0","")
        
        s = bin(len(s))[2:]
        count += 1
        
    return [count,zero]

## 풀이전략, 핵심 아이디어
# 반복해야 하는 조건이 명확하므로 while 사용
# 개수, 이진변환 반복하며 개수 세기
