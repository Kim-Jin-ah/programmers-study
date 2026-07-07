def solution(number, limit, power):
    numlist = []
    
    for i in range(1,number+1):
        count = 0
        for j in range(1,int(i**0.5)+1):
            if i % j == 0:
                if j == i // j:
                    count += 1
                else:
                    count += 2
            
        if count > limit:
            count = power
        numlist.append(count)
        
            
    return sum(numlist)

## 풀이전략, 핵심 아이디어
# 효율성을 생각한 답을 고려하는 방식을 더욱 고민해봐야함
# 이중반복문에서 루트씌운 숫자까지만 검사하고, count를 +1할지 +2할지만 if문으로 거르기
# 끝까지 검사하지 않고 줄일 수 있는 방법 찾기
# 나머지는 약수 찾는 문제와 유사
