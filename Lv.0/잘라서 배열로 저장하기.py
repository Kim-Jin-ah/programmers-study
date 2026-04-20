def solution(my_str, n):
    answer = []
    for i in range(0,len(my_str),n):
        answer.append(my_str[i:i+n])
    return answer

## 풀이전략, 핵심아이디어
# range 함수의 범위 활용
# n씩 끊고, 그 이후에 끊은 것도 나와야 하므로 append 사용해야함
