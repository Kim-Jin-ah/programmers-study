def solution(diffs, times, limit):
    start = 1
    end = max(diffs)
    answer = end

    while start <= end:
        mid = (start + end) // 2
        
        total = 0
        for i in range(len(diffs)):
            if diffs[i] <= mid:
                total += times[i]
            else:
                count = diffs[i] - mid
                if i == 0:
                    total += ((times[1] * count)+ times[1])
                else:
                    total += ((times[i]+times[i-1]) * count + times[i])
                    
        if total <= limit:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
    
    return answer

## 풀이전략, 핵심 아이디어
# 중간값(임의의 숙련도)로 모든 퍼즐을 풀었을 때 시간을 비교하며 근접하기가 핵심!!
