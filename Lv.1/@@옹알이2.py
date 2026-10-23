def solution(babbling):
    answer = 0
    words = ["aya","ye","woo","ma"]
    
    for s in babbling:
        check = True
        
        for w in words:
            if w * 2 in s:
                check = False
        if not check:
            continue
        
        for w in words:
            s = s.replace(w," ")
            
        if s.strip() == "":
            answer += 1
        
    return answer

## 풀이전략, 핵심 아이디어
# 연속으로 나오는 것을 제외하는 것이 핵심
# 조건에 맞지 않는 경우 현재 반복만 건너뛰고 다음 문자열 검사하는 패턴 익히기!!
