def solution(wallpaper):
    answer = []
    start = []
    end = []
    for i in range(len(wallpaper)):
         for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == "#":
                start.append((i,j)) 
                end.append((i+1,j+1))
    
    li = []
    answer.append(start[0][0])
    for s in start:
        li.append(s[1])
        li.sort()
    answer.append(li[0])
    li = []
        
    answer.append(end[-1][0])
    for e in end:
        li.append(e[1])
        li.sort(reverse=True)
    answer.append(li[0])
    li = []
    
    return answer
# 풀이전략, 핵심 아이디어
# 위의 방식은 너무 비효율적이야.. 
# 처음에 행,열 초기화하고 최소,최대를 찾는 방식으로 접근
def solution(wallpaper):
    min_row = len(wallpaper) # 행의개수
    min_col = len(wallpaper[0]) # 열의개수
    
    max_row = 0
    max_col = 0
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == "#":
                min_row = min(min_row, i)
                min_col = min(min_col, j)
                
                max_row = max(max_row, i)
                max_col = max(max_col, j)
    return [min_row, min_col, max_row + 1, max_col +1]
