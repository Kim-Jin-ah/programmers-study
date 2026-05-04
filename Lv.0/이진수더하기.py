def solution(bin1, bin2):
    answer = ''
    answer = bin(int(bin1,2)+int(bin2,2))[2:]
    return answer

## 풀이전략, 핵심아이디어
# 2진수 문자열을 10진수로 바꿔 계산한 후
# bin()을 이용해 10진수에서 2진수로 변경
# 추가로 [2:]로 슬라이싱
