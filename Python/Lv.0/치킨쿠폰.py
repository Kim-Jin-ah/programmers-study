def solution(chicken):
    answer = 0
    while chicken >= 10:
        new = chicken // 10
        answer += new
        chicken = new + (chicken % 10)
    return answer

## 풀이전략, 핵심아이디어
# while을 통해 쿠폰이 10장 미만이 될 때까지 돌리기
