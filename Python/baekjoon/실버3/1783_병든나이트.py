import sys
# from io import StringIO

# test_input = """100 50
# """

# sys.stdin = StringIO(test_input)
input = sys.stdin.readline

def solve():
    n,m = map(int,input().split())
    if n == 1:
        answer = 1
    elif n == 2:
        answer = min(4,(m+1)//2)
    else:
        if m < 7:
            answer = min(4,m)
        else:
            answer = m-2

    return answer

if __name__ == "__main__":
    print(solve())

## 풀이전략, 핵심 아이디어
# 세로가 1인지, 2인지, 3이상인지에 따라 이동 가능성이 달라진다 가 포인트
# 조건을 분석해서 최댓값을 구하는 그리디 문제
