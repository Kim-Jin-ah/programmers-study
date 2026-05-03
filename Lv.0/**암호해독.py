def solution(cipher, code):
    answer = ''
    for i in range(code-1, len(cipher), code):
        answer += cipher[i]
        
    return answer

## 풀이전략, 핵심아이디어
# 범위를 정할때, 인덱스가 0부터 시작한다는 점 고려해야함
# code마다 나와야하니까, 간격은 code로 하고, 시작점을 code-1로 하면 index 3번이 나오게 됨!!

# 나중에 복습 필요
