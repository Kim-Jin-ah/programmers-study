def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i]*b[i]
    return answer

## 풀이전략, 핵심 아이디어
# a와 b의 길이가 같기 때문에 len(a) 만큼 반복문 돌림. len(b)여도 상관없을듯
# 반복문 안에서 같은 순번끼리 곱해서 더하기
