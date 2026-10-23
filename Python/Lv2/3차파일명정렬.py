def solution(files):
    answer = []
    
    for file in files:
        head = ""
        number = ""
        tail = ""
        
        i = 0
        while i < len(file) and not file[i].isdigit():
            head += file[i]
            i += 1
        while i < len(file) and file[i].isdigit():
            number += file[i]
            i += 1
        tail = file[i:]
        
        answer.append((head,int(number),tail,file))
    
    answer.sort(key=lambda x:(x[0].lower(),x[1]))
    
    return [x[3] for x in answer]

## 풀이전략, 핵심 아이디어
# 문자열 파싱 + 정렬 문제
# 어떤 기준으로 분리하는지 확인, 어떤 기준으로 정렬하는지 이해하기
