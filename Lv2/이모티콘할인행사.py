from itertools import product
def solution(users, emoticons):
    discounts = [10,20,30,40]
    arr = []
    for com in product(discounts,repeat=len(emoticons)):
        count = 0
        total = 0
        for user in users:
            money = 0
            for i in range(len(emoticons)):
                num = 100-com[i]
                if user[0] <= com[i]:
                    money += emoticons[i] * num / 100
                
            if money >= user[1]:
                count += 1
            else:
                total += money
                
        arr.append((count,total))
    arr.sort(key = lambda x : (x[0],x[1]),reverse = True)
    return arr[0]

## 풀이전략, 핵심 아이디어
# product를 사용해 중복순열을 만들어 시작하는 것이 핵심!
