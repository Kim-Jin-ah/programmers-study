def solution(money):
    answer = [0,0]
    answer[0] = money // 5500
    answer[1] = money % 5500
    return answer

## 풀이전략, 핵심아이디어
# 0번째와 1번째에 각각의 연산한 값을 넣어주는 문제
