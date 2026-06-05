def solution(s):
    answer = ''
    if len(s) % 2 == 1:
        answer = s[len(s)//2]
    else:
        answer = s[(len(s)//2 -1):(len(s)//2)+1]
    return answer

## 풀이전략, 핵심 아이디어
# 짝수 홀수 구분 먼저
# len(s) // 2 활용하여 결과 반환
# 슬라이싱 할 때 [시작:끝+1] 해야한다는 점 주의
