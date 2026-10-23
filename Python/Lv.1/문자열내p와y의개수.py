def solution(s):
    s = s.lower()
    return s.count("p") == s.count("y")

## 풀이전략, 핵심 아이디어
# lower()로 소문자로 바꾸고
# count()로 개수 세기
