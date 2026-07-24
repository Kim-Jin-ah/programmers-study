def solution(today, terms, privacies):
    answer = []
    dic_term = {}
    
    for t in terms:
        kind, month = t.split()
        dic_term[kind] = int(month)
    
    ty,tm,td = map(int,today.split("."))
    today_days = td + tm*28 + ty*28*12
        
    for idx, p in enumerate(privacies, start=1):
        date, kind = p.split()
        
        y,m,d = map(int,date.split("."))
        privacy_days = d + m*28 + y*28*12
        expire = privacy_days + dic_term[kind]*28
    
        if today_days >= expire:
            answer.append(idx)
            
    return answer

## 풀이전략, 핵심 아이디어
# terms -> 딕셔너리, 총일수 구하기, privacies 반복문 돌리면서 총일수 계산, 만료 여부 확인 순으로 진행
# split()으로 분히라고 "날짜를 하나의 숫자로 변환해서 비교한다" 가 핵심 !!
