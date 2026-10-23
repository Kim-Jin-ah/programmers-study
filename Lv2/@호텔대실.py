def solution(book_time):
    timeline = [0] * 1450

    for start, end in book_time:
        start_hour, start_minute = map(int, start.split(":"))
        end_hour, end_minute = map(int, end.split(":"))

        start_time = start_hour * 60 + start_minute
        end_time = end_hour * 60 + end_minute + 10

        timeline[start_time] += 1
        timeline[end_time] -= 1

    answer = 0
    rooms = 0

    for count in timeline:
        rooms += count
        answer = max(answer, rooms)

    return answer

## 풀이전략, 핵심 아이디어
# 각 시간의 입실과 청소 완료 변화를 기록한 뒤, 시간순으로 누적해서 동시에 사용중인 방의 최댓값을 구한다
# 진짜....어려움..............큰일이다 진짜//
