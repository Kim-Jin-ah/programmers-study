import sys
# from io import StringIO

# test_input = """10 4 2 10
# """

# sys.stdin = StringIO(test_input)
input = sys.stdin.readline

def solve():
    n,l,w,h = map(int,input().split())
    left = 0
    right = min(l,w,h)

    for _ in range(100):
        mid = (left+right) / 2
        cnt = int(l/mid) * int(w/mid) * int(h/mid)

        if cnt >= n:
            left = mid
        else:
            right = mid

    return left

if __name__ == "__main__":
    print(solve())

## 풀이전략, 핵심 아이디어
# 이분 탐색으로 가능한 길이를 절반씩 좁혀 나감
# n개 이상 들어간다면 길이를 늘리고, n개 미만이라면 길이를 줄이는 방식으로
