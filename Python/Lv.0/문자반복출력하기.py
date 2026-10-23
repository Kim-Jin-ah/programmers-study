def solution(my_string, n):
    answer = ''
    for i in my_string:
        answer += i * n
    return answer

## 풀이전략, 핵심 아이디어
# 별출력하기 문제와 거의 유사함
# 반복문 돌려 각각을 n번씩 추가하면 됨
