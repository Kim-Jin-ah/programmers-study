a, b = map(int, input().strip().split(' '))
for i in range(b):
    print("*" * a)

## 풀이 전략, 핵심 아이디어
# 문자열의 곱셈 주의
# b번만큼 행 반복 + a번만큼 "*" 찍기
