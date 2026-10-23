def solution(array):
    answer = 0
    for i in array:
        answer+=str(i).count('7')
    return answer

## 풀이전략, 핵심아이디어
# 각 숫자를 문자열로 변환하여, 문자 7을 찾는 것이 핵심
  
# 문자열로 바꾸지 않으면 7을 찾는다는 걸 적용했을 때 일의 자리에 7이 있는 경우에만 나옴
# 따라서, 그 경우엔 %10으로 자릿수 나누기를 해야함
# def solution(array):
#    answer = 0
#    for num in array:
#        while num > 0:
#            if num % 10 == 7:
#                answer += 1
#            num //= 10
#    return answer  이렇게
