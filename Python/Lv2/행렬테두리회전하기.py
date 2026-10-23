def solution(rows, columns, queries):
    matrix = []
    num = 1
    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(num)
            num += 1
        matrix.append(row)
    
    answer = []
    for query in queries:
        x1,y1,x2,y2 = query
        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1
        
        prev = matrix[x1][y1]
        minimum = prev
        
        for y in range(y1, y2):
            matrix[x1][y + 1], prev = prev, matrix[x1][y + 1]
            minimum = min(minimum, prev)

        for x in range(x1, x2):
            matrix[x + 1][y2], prev = prev, matrix[x + 1][y2]
            minimum = min(minimum, prev)

        for y in range(y2, y1, -1):
            matrix[x2][y - 1], prev = prev, matrix[x2][y - 1]
            minimum = min(minimum, prev)

        for x in range(x2, x1, -1):
            matrix[x - 1][y1], prev = prev, matrix[x - 1][y1]
            minimum = min(minimum, prev)
            
        answer.append(minimum)
        
    return answer

## 풀이전략, 핵심 아이디어
# prev가 숫자를 하나씩 전달하면서 테두리를 한바퀴 도는 과정을 이해하고 쓸 줄 알아야함..
