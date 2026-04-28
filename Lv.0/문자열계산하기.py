def solution(my_string):
    answer = 0
    string = my_string.split()
    answer = int(string[0])
    
    for i in range(1,len(string),2):
        op = string[i]
        num = int(string[i+1])
        
        if op == "+":
            answer += num
        else:
            answer -= num
            
    return answer

## 풀이 전략, 핵심 아이디어
# int와 str을 구분하는 게 포인트!
# 첫번째는 무조건 int니까 먼저 제외
# 이후부터 str, int로 반복 이용하기
# 추가로 str로 연산자 비교한 뒤 +,- 계산하기
