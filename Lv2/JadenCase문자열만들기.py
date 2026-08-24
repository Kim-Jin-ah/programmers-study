def solution(s):
    answer = []
    words = s.split(" ")
    
    for word in words:
        if word == "":
            answer.append("")
        else:
            word = word[0].upper() + word[1:].lower()
            answer.append(word)
        
    return " ".join(answer)

## 풀이전략, 핵심 아이디어
# split()과 split(" ") 사용의 차이 => 공백 개수 유지 가능 - 알아두기
