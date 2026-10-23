def solution(babbling):
    answer = 0
    words=["aya","ye","woo","ma"]
    
    for s in babbling:
        for w in words:
            s = s.replace(w," ")
            
        if s.strip()=="":
            answer+=1
    return answer

## 풀이전략, 핵심아이디어
# babbling 리스트 입력 받고
# 각 문자열 꺼낸 뒤, 하나씩 검사
# 해당되는 것들은 공백으로
# 공백 조건이 맞다면 개수 증가시키기
