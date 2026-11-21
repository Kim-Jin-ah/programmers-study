def solution(gems):
    answer = [0,len(gems)-1]
    total = len(set(gems))
    shopping = {}
    left = 0
    
    for right in range(len(gems)):
        gem = gems[right]
        shopping[gem] = shopping.get(gem,0) + 1
        
        while len(shopping) == total:
            if right - left < answer[1] - answer[0]:
                answer = [left,right]
            
            shopping[gems[left]] -= 1
            
            if shopping[gems[left]] == 0:
                del shopping[gems[left]]
            
            left += 1
            
    return [answer[0]+1,answer[1]+1]

## 풀이전략, 핵심 아이디어
# 슬라이딩 윈도우와 투 포인터 사용
# 모든 종류의 보석을 포함하는 끝 인덱스를 찾고 왼쪽 인덱스에서 시작해 줄여나가기
