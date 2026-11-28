import sys
# from io import StringIO

# test_input = """C1 B1 3
# L
# T
# LB
# """

# sys.stdin = StringIO(test_input)
input = sys.stdin.readline

def solve():
    king,stone,N = input().split()
    todo = [input().strip() for _ in range(int(N))]

    dic = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7}
    directions = {"R":(1,0),"L":(-1,0),"B":(0,-1),"T":(0,1),"RT":(1,1),"LT":(-1,1),"RB":(1,-1),"LB":(-1,-1)}

    kx = dic[king[0]]
    ky = int(king[1])-1

    sx = dic[stone[0]]
    sy = int(stone[1])-1

    for d in todo:
        dx,dy = directions[d]
        nx,ny = kx+dx,ky+dy

        if not (0 <= nx < 8 and 0 <= ny < 8):
            continue

        if nx == sx and ny == sy:
            nsx, nsy = sx + dx, sy + dy
            if not (0 <= nsx < 8 and 0 <= nsy < 8):
                continue
            sx, sy = nsx, nsy

        kx, ky = nx, ny
            
    answer = [0,0]
    for key,value in dic.items():
        if value == kx:
            answer[0] = key+str(ky+1)
        if value == sx:
            answer[1] = key+str(sy+1)

    return "\n".join(answer)

if __name__ == "__main__":
    print(solve())

// 풀이전략, 핵심 아이디어
// 간결성과 가독성 신경쓰기
// continue를 먼저 쓴 다음 두 가지 경우 분리. 같은 경우 두 번 쓰지 않기
