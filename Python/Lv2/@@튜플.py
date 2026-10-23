def solution(s):
    s = s[2:-2]
    sets = s.split("},{")
    sets.sort(key=lambda x:len(x.split(",")))
    
    answer = []
    for i in sets:
        numbers = i.split(",")
        
        for num in numbers:
            num = int(num)
            if num not in answer:
                answer.append(num)
                
    return answer

## set을 이용한 방법
def solution(s):
    s = s[2:-2]
    sets = s.split("},{")
    sets.sort(key=lambda x:len(x.split(",")))
    
    answer = []
    used = set()
    
    for i in sets:
        numbers = i.split(",")
        
        for num in numbers:
            num = int(num)
            if num not in used:
                answer.append(num)
                used.add(num)
    return answer

## 풀이전략, 핵심 아이디어
# 발상의 전환 필요!!
# 알고 있는 문법을 다양한 방법으로 활용할 수 있어야 함..
