def solution(num_list, n):
    answer = []
    
    for i in range(0,len(num_list),n):
        answer.append(num_list[i:i+n])
        
    return answer

## 풀이전략, 핵심 아이디어
# 2차원배열로 만든다는 말에 겁먹지 말자.
# 슬라이싱 + step 이동만 잘 쓰면 충분히 풀 수 있음..
