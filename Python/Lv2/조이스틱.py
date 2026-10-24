def solution(name):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dic = {"A":0}
    count = 1
    for i in range(1,len(alpha)//2+1):
        dic[alpha[i]] = count
        dic[alpha[-i]] = count
        count += 1
    
    answer = 0
    n = len(name)
    
    for c in name:
        answer += dic[c]
    
    move = n-1
    for i in range(n):
        next_i = i+1
        while next_i < n and name[next_i] == "A":
            next_i += 1
        
        move = min(move,2*i + n - next_i)
        move = min(move,i + 2*(n-next_i))
    
    return answer + move

## 풀이전략, 핵심 아이디어
# 알파벳은 딕셔너리로, 커서 이동은 따로 반복문 사용
# move 공식 세우는 것, while문으로 돌리는 조건 이 핵심
