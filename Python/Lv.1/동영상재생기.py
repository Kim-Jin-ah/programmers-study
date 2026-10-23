def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    vm,vs = video_len.split(":")
    vm,vs = int(vm),int(vs)
    vl = vm*60 + vs
    pm,ps = pos.split(":")
    pm,ps = int(pm),int(ps)
    pl = pm*60 + ps
    
    start_m,start_s = op_start.split(":")
    start_m,start_s = int(start_m),int(start_s)
    osl = start_m*60 + start_s
    oem,oes = op_end.split(":")
    oem,oes = int(oem),int(oes)
    oel = oem*60 + oes
    
    if osl <= pl <= oel:
        pl = oel
            
    for com in commands:   
        if com == "next":
            if pl + 10 > vl:
                pl = vl
            else:
                pl += 10
            
        elif com == "prev":
            if pl - 10 < 0:
                pl = 0
            else:
                pl -= 10
                
        if osl <= pl <= oel:
            pl = oel
        
    mm = str(pl // 60)
    ss = str(pl % 60)
    return mm.zfill(2) + ":" + ss.zfill(2)

## 풀이전략, 핵심 아이디어
# 시간을 모두 초 단위로 변환해서 계산하는 것이 핵심
# 초로 변환 -> 시작 위치가 오프닝이면 이동 -> 명령어 실행 -> 명령어 실행 후 오프닝 여부 확인 -> 다시 mm:ss 형식으로 변환
