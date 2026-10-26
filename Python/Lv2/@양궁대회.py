def solution(n, info):
    answer = [-1]
    max_diff = 0
    ryan = [0] * 11

    def dfs(idx, left):
        nonlocal answer, max_diff

        if idx == 10:
            ryan[10] = left

            apeach_score = 0
            ryan_score = 0

            for i in range(10):
                score = 10 - i

                if info[i] == 0 and ryan[i] == 0:
                    continue

                if ryan[i] > info[i]:
                    ryan_score += score
                else:
                    apeach_score += score

            diff = ryan_score - apeach_score

            if diff > max_diff:
                max_diff = diff
                answer = ryan[:]

            elif diff > 0 and diff == max_diff:
                if ryan[::-1] > answer[::-1]:
                    answer = ryan[:]

            return

        ryan[idx] = 0
        dfs(idx + 1, left)

        need = info[idx] + 1

        if left >= need:
            ryan[idx] = need
            dfs(idx + 1, left - need)

        ryan[idx] = 0

    dfs(0, n)

    return answer

## 풀이전략, 핵심 아이디어
# dfs(0, n) 실행
# 점수 구간을 포기하는 경로 탐색
# 점수 구간을 획득하는 경로 탐색
# 각 경로에서 idx == 10에 도달하면 점수를 계산하고 복귀
# 복귀한 위치에서 ryan[idx] = 0 실행
# 현재 단계의 다른 선택지도 탐색
# 모든 탐색이 끝나면 dfs(0, n) 호출 자체가 종료
# 마지막으로 return answer 실행
