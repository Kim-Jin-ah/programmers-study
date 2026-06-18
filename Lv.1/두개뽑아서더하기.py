def solution(numbers):
    answer = set()
    
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            answer.add(numbers[i] + numbers[j])
        
    return sorted(answer)

## 풀이전략, 핵심 아이디어
# 이중반복문 사용
# set()을 중복 제거용으로 사용. (단, 본질은 함수가 아니라 집합자료형임을 기억하기)

# 비슷한 다른 방법으로는
def solution(numbers):
    answer = set()

    for idx, num in enumerate(numbers):
        for i in range(idx + 1, len(numbers)):
            answer.add(num + numbers[i])

    return sorted(answer)
# enumerate()를 사용하여 값,인덱스 모두 활용
