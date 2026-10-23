def solution(cards1, cards2, goal):
    
    for word in goal:
        if cards1 and cards1[0] == word:
            cards1.pop(0)
        elif cards2 and cards2[0] == word:
            cards2.pop(0)
        else:
            return "No"
        
    return "Yes"

## 풀이전략, 핵심 아이디어
# 조건문에서 cards1 and 로 비어있는지 아닌지 먼저 확인 -> 핵심!!
# 비어있으면 에러가 나기 때문에 이런 형식 무조건 기억하기!!

# 맞는 단어 있으면 맨 앞 단어 지우기 반복
