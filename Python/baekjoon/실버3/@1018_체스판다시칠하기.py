import sys
# from io import StringIO

# test_input = """10 13
# BBBBBBBBWBWBW
# BBBBBBBBBWBWB
# BBBBBBBBWBWBW
# BBBBBBBBBWBWB
# BBBBBBBBWBWBW
# BBBBBBBBBWBWB
# BBBBBBBBWBWBW
# BBBBBBBBBWBWB
# WWWWWWWWWWBWB
# WWWWWWWWWWBWB
# """

# sys.stdin = StringIO(test_input)
input = sys.stdin.readline
def solve():
    n,m = map(int,input().split())
    board = [input().strip() for _ in range(n)]
    answer = 64

    for i in range(n-7):
        for j in range(m-7):
            countw = 0

            for r in range(8):
                for c in range(8):
                    curr = board[i+r][j+c]

                    if (r+c) % 2 == 0:
                        if curr != "W":
                            countw += 1
                    else:
                        if curr != "B":
                            countw += 1

            countb = 64 - countw
            answer = min(answer,countw,countb)

    return answer

if __name__ == "__main__":
    print(solve())

## 풀이전략, 핵심 아이디어
# 좌상단이 'W' 또는 'B'로 시작된다 라는 패턴을 활용하여 완전탐색 진행
# answer를 우선적으로 64로 잡은 이유 기억해두기
