import sys
from collections import deque
# from io import StringIO

# test_input = """10 3
# 2 9 5
# """

# sys.stdin = StringIO(test_input)
input = sys.stdin.readline

def solve():
    n,m = map(int,input().split())
    targets = list(map(int,input().split()))
    queue = deque(range(1,n+1))
    answer = 0

    for target in targets:
        idx = queue.index(target)

        if idx <= len(queue)//2:
            answer += idx
            queue.rotate(-idx)
        else:
            right = len(queue) - idx
            answer += right
            queue.rotate(right)

        queue.popleft()

    return answer

if __name__ == "__main__":
    print(solve())

## 풀이전략, 핵심 아이디어
# 원하는 숫자의 위치를 찾고 왼쪽 이동 횟수와 오른쪽 이동 횟수를 비교해서 더 적은 쪽으로 회전시키기 가 핵심
