def solution(my_string):
    answer = 0
    for i in my_string:
        if i.isdigit():
            answer += int(i)
    return answer

## 풀이전략, 핵심 아이디어
# isdigit()이 숫자인지 검사하는 것이라는 사실만 알면 바로 풀 수 있는 문제
# isdigit() 외워! 써먹어!!
