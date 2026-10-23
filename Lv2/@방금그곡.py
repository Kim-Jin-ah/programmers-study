def solution(m, musicinfos):
    def change(music):
        music = music.replace("C#", "c")
        music = music.replace("D#", "d")
        music = music.replace("F#", "f")
        music = music.replace("G#", "g")
        music = music.replace("A#", "a")
        return music

    m = change(m)
    answer = "(None)"
    max_time = 0
    
    for musicinfo in musicinfos:
        start,end,title,music = musicinfo.split(",")
        a,b = start.split(":")
        c,d = end.split(":")
        minus = (60*int(c) + int(d)) - (60*int(a) + int(b))
      
        music = change(music)
        
        if len(music) < minus:
            music = music * (minus // len(music)+1)
            
        music = music[:minus]
        
        if m in music:
            if minus > max_time:
                max_time = minus
                answer = title

    return answer

## 풀이전략, 핵심 아이디어
# 반복재생처리와 #처리가 핵심
# 충분히 반복된 music을 만들어주고, #이 붙은 문자를 다른 문자로 치환해 비교하기
