def solution(cacheSize, cities):
    #25
    cache = []
    answer = 0
    
    for city in cities:
        city = city.lower()
        
        if city in cache:
            answer += 1
            cache.remove(city)
            cache.append(city)
        else:
            answer += 5
            
            if cacheSize > 0:
                if len(cache) == cacheSize:
                    cache.pop(0)
                    
                cache.append(city)
                
    return answer

## 풀이전략, 핵심 아이디어
# 알고리즘 자체보다 LRU의 의미를 이해하는 것이 핵심
# 캐시에 있으면 꺼내서 맨 뒤로, 캐시에 없으면 맨 뒤에, 꽉 차 있으면 맨 앞 삭제
