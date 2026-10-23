def solution(begin, end):
    answer = []
    for n in range(begin,end+1):
        if n == 1:
            answer.append(0)
            continue
        
        block = 1
        for i in range(2,int(n**0.5)+1):
            if n % i == 0:
                if n // i <= 10000000:
                    block = n // i
                    break
                else:
                    block = i
        answer.append(block)
    return answer

## 풀이전략, 핵심 아이디어
# 약수는 루트씌운 값까지만 탐색하는 것이 효율적
# 블록 번호가 10000000을 초과하면 사용할 수 없으므로 이 내용도 조건식에 포함시켜야함
