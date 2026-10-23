def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
            answer.sort()
    if answer == []:
        return [-1]
    return answer

## 풀이전략, 핵심 아이디어
# arr에서 divisor로 나누어 떨어지는 숫자만 골라서
# 오름차순 정렬해 반환
# if answer == [] 는 len(answer) == 0 으로도 가능
