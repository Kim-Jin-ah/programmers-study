def solution(s):
    answer = []
    last = {}
    
    for i, ch in enumerate(s):
        if ch in last:
            answer.append(i - last[ch])
        else:
            answer.append(-1)
            
        last[ch] = i
        
    return answer

## 풀이전략, 핵심 아이디어
# 딕셔너리를 떠올려 "last[ch] = 현재 인덱스" 활용하는 것이 핵심
# 딕셔너리를 반복문과 같이 쓰는 문제 풀이 방법 더 익혀야 함
# 리스트일 경우 append로 추가하는 것 잊지 말고, 공식 외워두기
