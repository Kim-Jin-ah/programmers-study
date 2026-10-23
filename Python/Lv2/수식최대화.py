from itertools import permutations
def solution(expression):
    operators = ["+","-","*"]
    numbers = []
    ops = []
    num = ''
    
    for char in expression:
        if char.isdigit():
            num += char
        else:
            numbers.append(int(num))
            ops.append(char)
            num = ''
    numbers.append(int(num))
    
    answer = 0
    for priority in permutations(operators):
        nums = numbers[:]
        oper = ops[:]
        
        for op in priority:
            i = 0
            while i < len(oper):
                if oper[i] == op:
                    if op == "+":
                        result = nums[i] + nums[i + 1]
                    elif op == '-':
                        result = nums[i] - nums[i + 1]
                    else:
                        result = nums[i] * nums[i + 1]
                    nums[i] = result
                    nums.pop(i+1)
                    oper.pop(i)
                else:
                    i += 1
        answer = max(answer,abs(nums[0]))
    return answer

## 풀이전략, 핵심 아이디어
# 발상의 전환 필요, 연산자와 숫자 분리 과정과 연산 과정 잘 봐두기
