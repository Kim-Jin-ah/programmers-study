import math
def solution(fees, records):
    dic = {}
    
    for record in records:
        dic[record[6:10]] = []
        
    for record in records:
        hour = int(record[:2])*60+int(record[3:5])
        num,ch = record[6:10],record[11]
        
        if ch == "I":
            dic[num].append(-hour)
        else:
            dic[num].append(hour)
            
    for key,value in dic.items():
        if len(value) % 2 != 0:
            dic[key].append(23*60 + 59)
        dic[key] = sum(value)
    
    result = sorted(dic.items(),key=lambda x:x[0])
    answer = []
    for x,y in result:
        if y <= fees[0]:
            answer.append(fees[1])
        else:
            c = math.ceil((y-fees[0])/fees[2])
            answer.append(fees[1] + c * fees[3])
            
    return answer

## 풀이전략, 핵심 아이디어
# 풀이과정은 괜찮지만, 문자열의 위치를 직접 잘라서 쓰는 방식보다 split()을 활용하는 것이 더 읽기 쉽고 범용적임
