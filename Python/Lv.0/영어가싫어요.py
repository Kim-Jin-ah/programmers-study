def solution(numbers):
    answer = 0
    num_dict = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    
    for word, digit in num_dict.items():
        numbers = numbers.replace(word,digit)
        
    return int(numbers)
    return answer

## 풀이전략, 핵심아이디어
# 딕셔너리, replace 이용
# 딕셔너리 넣은 반복문 형태 재복습 필요
