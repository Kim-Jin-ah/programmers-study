def solution(array, n):
    answer = array[0]
    for num in array:
        if abs(num-n) < abs(answer-n):
            answer = num
        elif abs(num-n) == abs(answer-n) and num <answer:
            answer = num
    return answer

## 풀이전략, 핵심아이디어
# 절댓값을 활용해야하는 문제
# answer를 array[0]으로 한 뒤 요소를 하나씩 꺼내서 n과의 차이를 비교하는 방식
# 차이가 같다면 더 작은 수를 정답으로 제출해야한다는 점을 고려해 and 조건으로 num<answer 넣기 주의
