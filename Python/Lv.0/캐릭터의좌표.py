def solution(keyinput, board):
    x = 0
    y = 0
    
    max_x = board[0] // 2
    max_y = board[1] // 2
    
    for key in keyinput:
        if key == "left":
            if x > -max_x:
                x -= 1
        elif key == "up":
            if y < max_y:
                y += 1
        elif key == "down":
            if y > -max_y:
                y -= 1
        elif key == "right":
            if x < max_x:
                x += 1

    return [x,y]

## 풀이전략, 핵심 아이디어
# 이동하기 전에 범위를 벗어나는지 검사 가 핵심!
# x,y와 최대로 갈 수 있는 max_x, max_y 이용
