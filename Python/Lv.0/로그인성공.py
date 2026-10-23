def solution(id_pw, db):
    answer = ''
    id1, pw1 = id_pw
    
    for mi, mp in db:
        if id1 == mi and pw1 == mp:
            return "login"
        elif id1 == mi:
            return "wrong pw"
    return "fail"
    return answer

## 풀이전략, 핵심아이디어
# 아이디와 비밀번호를 분리하여 각각의 요소 일치 확인
