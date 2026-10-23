def solution(s):
    if len(s) == 4 or len(s) == 6:
        return s.isdigit()
    return False

## 풀이전략, 핵심 아이디어
# 길이 확인, 숫자인지 확인하는 각각 함수 용도 기억하기

# 짧게 바꾼다면?
def solution(s):
  return (len(s) == 4 or len(s) == 6) and s.isdigit()
