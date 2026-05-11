def solution(polynomial):
    x_coef = 0
    const = 0
    
    terms = polynomial.split(" + ")
    
    for term in terms:
        if "x" in term:
            if term == "x":
                x_coef += 1
            else:
                x_coef += int(term[:-1])
        else:
            const += int(term)
    
    answer = ""
    if x_coef:
        if x_coef == 1:
            answer += "x"
        else:
            answer += str(x_coef) + "x"
    
    if const:
        if answer:
            answer += " + "
        answer += str(const)
        
    return answer

## 풀이전략, 핵심 아이디어
# 문자열 분리 후 x항,상수항 구분하고 문자열을 조립하여 결과로 제출하는 과정
# 하나하나씩 뜯어서 생각하기
# 공백 실수하지 말기
# x의 계수가 -1번째 라는 것 기억하기
# if 와 else 위치 신경쓰기
