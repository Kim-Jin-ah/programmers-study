def solution(n, arr1, arr2):
    answer = []
    
    for a,b in zip(arr1,arr2):
        row = bin(a|b)[2:]
        row = row.rjust(n,'0')
        
        row = row.replace('1','#')
        row = row.replace('0',' ')
        
        answer.append(row)
        
    return answer

## 풀이전략, 핵심 아이디어
# zip()으로 묶기, 비트 OR 연산 이용, rjust()로 0 채우기, replace로 문자 바꾸기
# 비트 연산에 대해 더 공부할 필요가 있음
