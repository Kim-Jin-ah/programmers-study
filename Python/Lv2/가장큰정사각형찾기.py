def solution(board):
    n = len(board)
    m = len(board[0])
    
    max_len = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                max_len = 1
                
    for i in range(1,n):
        for j in range(1,m):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j], board[i][j-1], board[i-1][j-1]) + 1
                max_len = max(max_len, board[i][j])
                
    return max_len * max_len

## 풀이전략, 핵심 아이디어
# 동적계획법 사용, 오른쪽 아래 꼭짓점을 기준으로 최솟값에 1을 더해 최대 찾기
