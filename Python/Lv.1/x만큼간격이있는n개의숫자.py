def solution(x, n):
    answer = []
    for i in range(1, n + 1):
        answer.append(x * i)
    return answer

## 풀이전략, 핵심 아이디어
# range의 의미를 잘 파악하고 활용을 잘해야함
# range(x,x*n+1,x)로 해서 푸니까 더 복잡하고 시간도 오래 걸림 -- 복잡하게 생각하지 말기..!

# 리스트 컴프리헨션을 사용한 방법
def solution(x, n):
    return [x * i for i in range(1, n + 1)]
