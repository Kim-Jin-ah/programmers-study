def solution(number):
    count = 0
    for i in range(len(number)):
        for j in range(i+1, len(number)):
            for k in range(j+1, len(number)):
                if number[i] + number[j] + number[k] == 0:
                    count += 1
    return count

## 풀이전략, 핵심 아이디어
# 각 3개를 뽑는 경우의 수를 3중 for문으로 활용
# 조합의 개념 이해하기
