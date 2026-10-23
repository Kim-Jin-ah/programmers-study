def solution(friends, gifts):
    n = len(friends)
    idx = {}
    for i,friend in enumerate(friends):
        idx[friend] = i
    
    cnt = [[0]*n for _ in range(n)]
    score = [0]*n

    for gift in gifts:
        giver,receiver = gift.split()
        a = idx[giver]
        b = idx[receiver]
        
        cnt[a][b] += 1
        score[a] += 1
        score[b] -= 1
    
    next_g = [0]*n
    
    for i in range(n):
        for j in range(i+1,n):
            if cnt[i][j] > cnt[j][i]:
                next_g[i] += 1
            elif cnt[i][j] < cnt[j][i]:
                next_g[j] += 1
            else:
                if score[i] > score[j]:
                    next_g[i] += 1
                elif score[i] < score[j]:
                    next_g[j] += 1    
    return max(next_g)

## 풀이전략, 핵심 아이디어
# dict을 이용해 문자열을 인덱스로 변환하기
# 2차원 리스트로 사람 간의 관계(선물횟수) 저장하기
# 준 횟수 - 받은 횟수 계산 후 비교
