def solution(n):
    answer = 0

    for i in str(n):
        answer += int(i)

    return answer

## 풀이전략, 핵심 아이디어
# for문에는 str을, 반복문 안의 i는 각각은 int로 더하기
