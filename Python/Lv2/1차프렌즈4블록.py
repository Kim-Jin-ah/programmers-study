def solution(m, n, board):
    board = [list(row) for row in board]
    answer = 0

    while True:
        remove = set()

        for i in range(m - 1):
            for j in range(n - 1):

                if board[i][j] == ".":
                    continue

                if (board[i][j] == board[i][j+1] ==
                    board[i+1][j] == board[i+1][j+1]):

                    remove.add((i, j))
                    remove.add((i, j+1))
                    remove.add((i+1, j))
                    remove.add((i+1, j+1))

        if not remove:
            break

        answer += len(remove)

        for i, j in remove:
            board[i][j] = "."
        
        for j in range(n):
            blocks = []

            for i in range(m):
                if board[i][j] != ".":
                    blocks.append(board[i][j])
                    
            for i in range(m - 1, -1, -1):
                if blocks:
                    board[i][j] = blocks.pop()
                else:
                    board[i][j] = "."
    return answer

## 풀이전략, 핵심 아이디어
# 진짜 어렵다....
# 나머지를 채우고 다시 시작한다는 부분에서 막힘 -> 코드를 다 쓰더라도 while로 인해 다시 돌아간다는 걸 인지하기
# 풀이순서 : 2*2 찾기 -> 삭제할 좌표를 set에 저장 -> set에 있는 블록을 전부 삭제 -> 블록을 아래로 떨어뜨림 -> 계속 반복
