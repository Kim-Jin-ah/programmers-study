def solution(my_string):
    answer = []
    for i in my_string:
        if i.isdigit():
            answer.append(int(i))
    answer.sort()
    return answer

## 풀이전략, 핵심아이디어
# answer를 [] 로 잡았기 때문에 append로 추가해야한다는 점 기억
