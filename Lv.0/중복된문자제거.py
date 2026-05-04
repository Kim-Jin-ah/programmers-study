def solution(my_string):
    answer = ''
    for s in my_string:
        if s not in answer:
            answer += s
    return answer

## 풀이전략, 핵심아이디어
# 반복문 돌리고 s not in answer 가 키포인트
# 각 문제에 어떤 문법이 들어갈지 활용하는 방법 더 익혀야할듯
