def solution(n):
    answer = ''
    for i in range(n):
        if i % 2 == 0:
            answer += '수'
        else:
            answer += '박'
    return answer

## 풀이전략, 핵심 아이디어
# 짝수번째 '수', 홀수번째 '박' 추가
