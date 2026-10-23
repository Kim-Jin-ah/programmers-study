def solution(arr):
    answer = [arr[0]]

    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            answer.append(arr[i])

    return answer

## 풀이 전략, 핵심 아이디어
# arr[0]을 미리 넣어두고 i = 1부터 시작
# 이전 값(arr[i-1])과 다를 때만 추가

# 이전 값과 같으면 버리고 다르면 추가한다는 것이 핵심
# 그것을 이용한 다른 쉬운 방법
def solution(arr):
    answer = []

    for num in arr:
        if not answer or answer[-1] != num:
            answer.append(num)

    return answer
