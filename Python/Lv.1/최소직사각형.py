def solution(sizes):
    arr1 = []
    arr2 = []
    for i in sizes:
        i = sorted(i,reverse=True)
        
        arr1.append(i[0])
        arr2.append(i[1])
                
    return max(arr1) * max(arr2)

## 풀이전략, 핵심 아이디어
# 회전시켜서 큰 변과 작은 변을 분리한다가 핵심인 문제

# 다만, 다른 더 쉬운 방법으로 풀도록 해볼것
def solution(sizes):
    w = []
    h = []

    for a, b in sizes:
        w.append(max(a, b))
        h.append(min(a, b))

    return max(w) * max(h)
