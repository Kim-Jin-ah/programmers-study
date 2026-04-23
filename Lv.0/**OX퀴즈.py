def solution(quiz):
    answer = []
    for q in quiz:
        a, op, b, _, c = q.split()
        a,b,c = int(a),int(b),int(c)
        
        if op == "+":
            result = a + b
        else:
            result = a - b
            
        if result == c:
            answer.append("O")
        else:
            answer.append("X")
    return answer

## 풀이전략, 핵심아이디어
# quiz 내 요소들을 분리하기 위해 split하고 구성요소 int 설정
# if 로 연산자와 결과 비교한 후 각 상황에 맞는 결과가 출력되도록 설정
# 따라서, 각 요소를 분리하고 설정하는 단계를 생각하는 것이 키포인트

# 많이 헤멘 문제.. 리스트 분리 기억하기
