def solution(strlist):
    answer = []
    for str in strlist:
        answer.append(len(str))
    return answer

## 풀이전략, 핵심 아이디어
# len() 함수를 사용하여 비어있는 answer에 추가하면 됨
