def solution(s):
    answer = 0
    dic = {"zero":"0","one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"}
    
    for key, value in dic.items():
        s = s.replace(key,value)
            
    return int(s)

## 풀이전략, 핵심 아이디어
# 딕셔너리로 key,value로 나눔
# replace() 로 치환 - 단, 문자,문자 형태여야 함 주의
# 문제 유형 알고 가기!
# 딕셔너리 버전 말고도
def solution(s):
    nums = [
        "zero", "one", "two", "three", "four",
        "five", "six", "seven", "eight", "nine"
    ]

    for i in range(10):
        s = s.replace(nums[i], str(i))

    return int(s)
# 이 방법도 가능
