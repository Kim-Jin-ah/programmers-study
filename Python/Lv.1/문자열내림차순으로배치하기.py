def solution(s):
    
    return ''.join(sorted(s,reverse=True))

## 풀이전략, 핵심 아이디어
# 문자열의 문자열들을 내림차순하면 각각 분리됨을 기억
# 따라서 마지막에 join 사용해서 합쳐야함

# 예전에 풀었던 정수 내림차순으로 배치하기와 유사한 문제
# 이 패턴 기억해두기
