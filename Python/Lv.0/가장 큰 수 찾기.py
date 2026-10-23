def solution(array):
    answer = []
    max_array = max(array)
    answer = max_array, array.index(max_array)
    return answer

## 풀이전략, 핵심아이디어
# list에서 max로 최대인 수를 찾고, 이어서 그 자리의 인덱스를 찾으면 됨
