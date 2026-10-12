def solution(places):
    answer = []
    for place in places:
        safe = 1
        for x in range(5):
            for y in range(5):
                if place[x][y] != "P":
                    continue
                for dx,dy in [(0,1),(1,0),(-1,0),(0,-1)]:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < 5 and 0 <= ny < 5:
                        if place[nx][ny] == "P":
                            safe = 0
                            break
                if safe == 0:
                    break
                for dx,dy in [(0,2),(2,0),(-2,0),(0,-2)]:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < 5 and 0 <= ny < 5:
                        if place[nx][ny] == "P":
                            mx = (x + nx) // 2
                            my = (y + ny) // 2
                            if place[mx][my] != "X":
                                safe = 0
                                break
                if safe == 0:
                    break
                for dx, dy in [(1,1),(1,-1),(-1,1),(-1,-1)]:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < 5 and 0 <= ny < 5:
                        if place[nx][ny] == 'P':
                            if place[x][ny] != 'X' or place[nx][y] != 'X':
                                safe = 0
                                break
                if safe == 0:
                    break
            if safe == 0:
                break
        answer.append(safe)
    return answer

## 풀이전략, 핵심 아이디어
# 규칙에 따라 직접 주변 좌표를 확인하는 구현. 3가지로 나누어 정리
