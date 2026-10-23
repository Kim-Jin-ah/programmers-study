def solution(id_list, report, k):
    report = list(set(report))
    answer = []
    dic = {}
    count = {}
    for user in id_list:
        dic[user] = []
        count[user] = 0
        
    for i in report:
        a,b = i.split()
        dic[a].append(b)
        count[b] += 1
           
    for user in id_list:
        mail = 0
        for reported in dic[user]:
            if count[reported] >= k:
                mail += 1
        answer.append(mail)

    return answer

## 풀이전략, 핵심 아이디어
# dic:누가 누구를 신고했는지 저장 / count:누가 몇번 신고당했는지 저장
# set으로 중복제거 잊지말자
