def solution(genres, plays):
    answer = []
    total = {} #장르별 총 재생 횟수
    songs = {} #장르별(재생횟수,고유번호) 저장
    
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        total[genre] = total.get(genre,0) + play
        
        if genre not in songs:
            songs[genre] = []
        songs[genre].append((play,i))
    
    genre_order = sorted(total,key=total.get,reverse=True)
    
    for genre in genre_order:
        songs[genre].sort(key=lambda x: (-x[0],x[1]))
        
        answer.extend([index for play,index in songs[genre][:2]])
        
    return answer

## 풀이 순서와 흐름 이해하기 - 딕셔너리 만든 과정, 아이디어 핵심!!
# 정렬 기준과 lambda의 쓰임새 기억하기
