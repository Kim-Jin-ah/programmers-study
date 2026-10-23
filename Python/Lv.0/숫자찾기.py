def solution(num, k):
    if str(k) in str(num):
        return str(num).index(str(k)) + 1
    else:
        return -1

## 풀이전략, 핵심아이디어
# 숫자를 문자열로 반환
# index()의 결과는 0부터 시작, 따라서 +1 필요
# in 활용 생각하기 + 너무 복잡하게 생각하지 않기
