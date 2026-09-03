def solution(land):
    for i in range(1,len(land)):
        land[i][0] += max(land[i-1][1], land[i-1][2], land[i-1][3])
        land[i][1] += max(land[i-1][0], land[i-1][2], land[i-1][3])
        land[i][2] += max(land[i-1][0], land[i-1][1], land[i-1][3])
        land[i][3] += max(land[i-1][0], land[i-1][1], land[i-1][2])

    return max(land[-1])

## 풀이전략, 핵심 아이디어
# DP 사용 - 각 칸에 '여기까지 왔을 떄의 최고 점수'를 적어놓기
# 각자의 최고를 더하고 마지막행에서의 max()를 return 하기
