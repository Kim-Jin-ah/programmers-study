def solution(n,a,b):
    count = 0
    
    while True:
        a = (a+1) // 2
        b = (b+1) // 2
        count += 1
        
        if a == b:
            return count

## 풀이전략, 핵심 아이디어
# 같은 대진 그룹에 들어감을 확인하기 위해 a=b 로 확인. 같으면 횟수(count) return
