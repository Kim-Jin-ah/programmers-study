def solution(num_list):
    answer = [0,0]
    for i in num_list:
        if i % 2 == 0:
            answer[0] += 1
        else:
            answer[1] += 1
    return answer

## 풀이전략, 핵심아이디어
# answer =[0,0] 으로 만들어놓고 인덱스를 활용하여
# 조건에 맞는 것들에 +1

# 다른 방법 참고
def solution(num_list):

    even = 0
    odd = 0

    for num in num_list:

        if num % 2 == 0:
            even += 1

        else:
            odd += 1

    return [even, odd]
