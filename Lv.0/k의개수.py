def solution(i, j, k):
    answer = 0
    for num in range(i,j+1):
        answer += str(num).count(str(k))
    return answer

## 풀이전략, 핵심아이디어
# 하나씩 검사해서 숫자를 올리는 방법 뿐만 아니라
# count로 개수를 한번에 세는 방법 또한 생각해보기
