def solution(board, h, w):
    n = len(board)
    count = 0
    
    dh = [0,1,-1,0]
    dw = [1,0,0,-1]
    
    for i in range(4):
        h_check = h + dh[i]
        w_check = w + dw[i]
        if 0 <= h_check < n and 0 <= w_check < n:
            if board[h][w] == board[h_check][w_check]:
                count += 1
    return count

## 풀이전략, 핵심 아이디어
# 네 방향 하나씩 확인
# 현재 위피에서 한칸 이동한 좌표 계산
# 이동한 좌표가 보드 안에 있는지 확인
# 이웃한 칸의 색이 현재 칸의 색과 같은지 비교. 같으면 +1
