def solution(numbers):
    answer = []
    for i in numbers:
        answer.append(i*2)
    return answer

## 풀이전략, 핵심 아이디어
# 배열을 반복하면서 각 원소에 2를 곱해 새 리스트 만들기
# 리스트 컴프리헨션으로 풀이해보기
def solution(numbers):
    return [i * 2 for i in numbers]
