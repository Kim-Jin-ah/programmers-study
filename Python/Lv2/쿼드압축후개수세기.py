def solution(arr):
    count = [0,0]
    
    def compress(x,y,size):
        first = arr[x][y]
        
        for i in range(x,x+size):
            for j in range(y,y+size):
                if arr[i][j] != first:
                    half = size // 2
                    
                    compress(x, y, half)
                    compress(x, y + half, half)
                    compress(x + half, y, half)
                    compress(x + half, y + half, half)

                    return

        count[first] += 1

    compress(0, 0, len(arr))

    return count

## 풀이전략, 핵심 아이디어
# 같으면 세고, 다르면 4등분해서 다시 확인
# 재귀 사용 부분이 중요. compress()
