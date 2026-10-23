def solution(food):
    answer = ''
    
    for i in range(1,len(food)):
        answer += str(i) * (food[i] // 2)
    
    return answer + '0' + answer[::-1]

## 풀이전략, 핵심 아이디어
# 배열 합칠 때 + 이용, 슬라이싱 활용이 부족했던 문제
# 왼쪽만 만들고 뒤집어서 오른쪽을 만들기
# 풀이 외우기!
