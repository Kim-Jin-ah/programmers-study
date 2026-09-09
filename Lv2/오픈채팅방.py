def solution(record):
    answer = []
    dic = {}
    for i in record:
        i = i.split(" ")
        
        if i[0] == "Enter":
            dic[i[1]] = i[2]
        elif i[0] == "Change":
            dic[i[1]] = i[2]
            
    for i in record:
        i = i.split(" ")
        
        if i[0] == "Enter":
            answer.append(f"{dic[i[1]]}님이 들어왔습니다.")
        elif i[0] == "Leave":
            answer.append(f"{dic[i[1]]}님이 나갔습니다.")

    return answer

## 풀이전략, 핵심 아이디어
# 딕셔너리 + 2번 순회 가 핵심
# 1차 순회로 아이디별 최종 닉네임을 확인하고, 딕셔너리 만들기
# 2차 순회에서 Enter와 Leave를 골라 최종 닉네임으로 메시지 생성하기
