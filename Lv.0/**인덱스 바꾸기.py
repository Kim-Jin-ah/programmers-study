def solution(my_string, num1, num2):
    answer = ''
    s = list(my_string)
    
    s[num1], s[num2] = s[num2], s[num1]
    return ''.join(s)

    return answer

## 풀이전략, 핵심아이디어
# 리스트로 변환 후 swap이 포인트!!
# 인덱스 교환 시 swap 활용 연습하기!!!
# 그 이후 join 으로 합치기
