def solution(a, b):
    
    month = [31,29,31,30,31,30,31,31,30,31,30,31]
    dayname = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED','THU']
    
    days = sum(month[:a-1]) +b
    
    return dayname[(days-1)%7]

## 풀이전략, 핵심 아이디어
# 리스트 활용, sum(), 나머지연산(%), 인덱스 계산 을 사용하는 규칙구현문제
# 리스트로 짜놓고 그걸 활용하여 합계와 나누기, 인덱스 고려한 풀이
# sum() 활용 더 익히기
