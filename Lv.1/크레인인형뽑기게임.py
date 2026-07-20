def solution(board, moves):
    answer = 0
    stack = []
    for i in moves:
        for j in board:
            if j[i-1] != 0:
                stack.append(j[i-1])
                j[i-1] = 0
                
                if len(stack) >= 2 and stack[-1] == stack[-2]:
                    stack.pop()
                    stack.pop()
                    answer += 2
                break       
    return answer

## 풀이전략, 핵심 아이디어
# 스택에 넣은 직후 검사
# break 위치 정확히 넣기
# 조건문 사용시 그 다음 조건을 어디에 넣을지 정확하게!!
# 순서 : move 하나 선택 -> 위에서부터 탐색 -> 0이 아니면 stack에 넣기, board는 0으로 만들기 -> stack의 마지막 두개 비교 후 같으면 제거 -> break 
