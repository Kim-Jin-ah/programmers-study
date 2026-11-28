import sys
# from io import StringIO

# test_input = """4 5
# adaca
# da##b
# abb#b
# abbac
# """

# sys.stdin = StringIO(test_input)
input = sys.stdin.readline

def solve():
    r,c = map(int,input().split())
    board = [list(input().strip()) for _ in range(r)]
    target = []

    for i in range(r):
        alpha = ""
        for j in range(c):
            if board[i][j] == "#":
                if len(alpha) >= 2:
                    target.append(alpha)
                alpha = ""

            else:
                alpha += board[i][j]

        if len(alpha) >= 2:
            target.append(alpha)

    for i in range(c):
        alpha = ""
        for j in range(r):
            if board[j][i] == "#":
                if len(alpha) >= 2:
                    target.append(alpha)
                alpha = ""

            else:
                alpha += board[j][i]

        if len(alpha) >= 2:
            target.append(alpha)

    target.sort()

    return target[0]

if __name__ == "__main__":
    print(solve())

## 풀이전략, 핵심 아이디어
# #을 만나면 지금까지 만든 단어 저장, 문자열 초기화
# #이 아니면 문자 계속 추가
# 반복문이 끝난 뒤 남은 단어도 저장 -> 포인트! 이런거 신경쓰는 연습 확실히 하자
