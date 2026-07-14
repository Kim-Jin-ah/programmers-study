def solution(lottos, win_nums):
    rank = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    count = 0
    zero = lottos.count(0)
    
    for i in lottos:
        if i in win_nums:
            count += 1
            
    return rank[count+zero],rank[count]

## 풀이전략, 핵심 아이디어
# 딕셔너리를 만들어 순위와 개수 연결
# 정답인 개수와 0인 개수를 나누고, 최소 최대로 return
