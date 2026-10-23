def solution(n, words):
    answer = [words[0]]
    s = words[0][-1]
    
    person = 1
    count = 1
    for i in range(1,len(words)):
        person = i % n + 1
        count = i // n + 1
        if not words[i].startswith(s) or words[i] in answer:
            return [person,count]
        
        s = words[i][-1]
        answer.append(words[i])
         
    return [0,0]
## 간단하게 하면
def solution(n, words):
    used = set()
    
    for i in range(len(words)):
        word = words[i]
        
        if word in used:
            return [i % n + 1, i // n + 1]

        if i > 0 and words[i-1][-1] != word[0]:
            return [i % n + 1, i // n + 1]
        
        used.add(word)
    
    return [0, 0]

## 풀이전략, 핵심 아이디어
# 몇 번째 사람인지, 몇 번째 차례인지 구하는 부분이 핵심
# 몫과 나머지 사용법 익히기
