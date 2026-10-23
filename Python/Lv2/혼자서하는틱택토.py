def check_win(board,char):
    wins = 0
    for row in board:
        if row.count(char) == 3:
            wins += 1
    for col in range(3):
        if board[0][col] == char and board[1][col] == char and board[2][col] == char:
            wins += 1
            
    if board[0][0] == char and board[1][1] == char and board[2][2] == char:
        wins += 1
        
    if board[0][2] == char and board[1][1] == char and board[2][0] == char:
        wins += 1
    
    return wins
def solution(board):
    o_count = sum(row.count("O") for row in board)
    x_count = sum(row.count("X") for row in board)
    
    if not (o_count == x_count or o_count == x_count+1):
        return 0
    
    o_win = check_win(board,"O")
    x_win = check_win(board,"X")
    
    if o_win > 0 and x_win > 0:
        return 0
    if o_win > 0 and o_count != x_count+1:
        return 0
    if x_win > 0 and o_count != x_count:
        return 0
    
    return 1

## 풀이전략, 핵심 아이디어
# 돌의 개수 비교와 승리 상태 판별을 조합하여 비정상적인 케이스를 필터링하는 방식으로 접근해야 하는 문제
# 시뮬레이션이 아닌 구현 이 포인트
