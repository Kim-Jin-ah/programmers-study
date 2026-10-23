def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    
    for i in range(0,len(score),m):
        if len(score[i:i+m]) == m:
            answer += min(score[i:i+m]) * m
        else:
            answer += 0
            
    return answer

## 여기서 else는 없어도 된다
## 내림차순이므로 min을 굳이 안써도 된다
## 반영해서 보완한다면
def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    
    for i in range(0, len(score), m):
        if i + m <= len(score):
            answer += score[i + m - 1] * m

    return answer
