def solution(answers):
    answer = []
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0,0,0]
    
    for i in range(len(answers)):
        if answers[i] == p1[i % len(p1)]:
            score[0] += 1
        if answers[i] == p2[i % len(p2)]:
            score[1] += 1
        if answers[i] == p3[i % len(p3)]:
            score[2] += 1
            
    max_score = max(score)
    for i in range(3):
        if score[i] == max_score:
            answer.append(i+1)
    return answer

## 풀이전략, 핵심 아이디어
# % 를 이용해서 반복되는 패턴을 표현하는 방법이 가장 중요. 외우기!
# 하나씩 대조 후 같으면 score에 넣음
# 이후 max인것 출력
