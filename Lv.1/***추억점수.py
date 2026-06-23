def solution(name, yearning, photo):
    answer = []
    dic = {}
    
    for i in range(len(name)):
        dic[name[i]] = yearning[i]
        
    for p in photo:
        score = 0
        
        for person in p:
            if person in dic:
                score += dic[person]
        
        answer.append(score)
    return answer

## 풀이전략, 핵심 아이디어
# 이름에 해당하는 점수를 찾아야하므로 딕셔너리가 적합함을 바로 떠올릴 수 있어야 함
# 딕셔너리로 바꾸는 방법, 이중리스트 반복문으로 풀어내는 방법 등 종합적으로 알고 있어야 함

# get()을 사용한 더 간단한 방법으로는
def solution(name, yearning, photo):
    answer = []

    dic = dict(zip(name, yearning))

    for p in photo:
        score = 0

        for person in p:
            score += dic.get(person, 0)

        answer.append(score)

    return answer
