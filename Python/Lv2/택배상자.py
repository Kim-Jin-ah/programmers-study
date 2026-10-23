def solution(order):
    stack = []
    answer = 0
    box = 1

    for target in order:
        while box <= len(order) and box < target:
            stack.append(box)
            box += 1

        if box == target:
            answer += 1
            box += 1
        elif stack and stack[-1] == target:
            stack.pop()
            answer += 1
        else:
            break

    return answer

## 풀이전략, 핵심 아이디어
# 현재 필요한 상자라면 바로 꺼내고, 아니면 보조 컨테이너에 넣는 것을 기억하고, stack을 보조 컨테이너 역할로 생각하고 활용
# 필요한 상자를 발견하면 +1, 보조 컨테이너에서 해당 상자를 pop()하면 +1, 더 이상 배송 불가능할 때 break로 종료
