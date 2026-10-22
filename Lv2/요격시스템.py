def solution(targets):
    targets.sort(key=lambda x: x[1])

    answer = 0
    last_end = 0

    for s, e in targets:
        if s >= last_end:
            answer += 1
            last_end = e

    return answer

## 풀이전략, 핵심 아이디어
# 끝점 기준 정렬, 새 요격 미사일 발사 조건 이 핵심
# >= 임 주의(경계선에선 요격이 불가능하므로)
