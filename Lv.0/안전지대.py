def solution(board):
    n = len(board)
    dx = [-1,-1,-1,0,0,1,1,1]
    dy = [-1,0,1,-1,1,-1,0,1]
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                for k in range(8):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                        board[nx][ny] = 2
    answer = 0
    for row in board:
        for v in row:
            if v == 0:
                answer += 1
                
    return answer

## 풀이전략, 핵심아이디어
# 2차원 배열을 사용하여 위치를 배열을 통해 이동하고 검사해야함
# 모서리 부분에 위치해 있을 가능성이 있기 때문에 if문으로 필터링
# 이러한 세팅 후, for문을 이용해 0인 곳 숫자세기
  
# 이런걸 내가 바로 풀 수 있을까....
