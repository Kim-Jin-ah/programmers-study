def solution(my_string):
    answer = ''
    string_low = my_string.lower()
    sorted_s = sorted(string_low)
    answer = ''.join(sorted_s)
    return answer

## 풀이전략, 핵심아이디어
# 정렬한 후 join으로 각 단어를 합쳐야한다는 것이 키포인트
# 문자를 분리해서 정렬해야한다는 점만 주의해서 다음에 다시 풀어보기
