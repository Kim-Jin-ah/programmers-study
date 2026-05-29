def solution(num_list):
    answer = []
    answer = num_list[::-1]
    return answer

## 풀이전략, 핵심 아이디어
# 문자열, 리스트 뒤집기에 자주 쓰이는 [::-1]을 사용하면 쉽게 풀리는 문제

# reverse()를 사용한 방법
def solution(num_list):
    answer = []
    num_list.reverse()
    answer = num_list
    return answer

# 여기서 answer = num_list.reverse() 가 아님 주의!!
