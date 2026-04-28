def solution(s1, s2):
    answer = 0
    for i in s1:
        for s in s2:
            if i == s:
                answer += 1
    return answer

## 풀이 전략, 핵심아이디어
# s1과 s2의 구성요소를 반복문을 통해 하나씩 꺼낸뒤
# 같은 것이 있는지 비교
# 같다면 +1 해주기
