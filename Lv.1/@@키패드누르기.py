def solution(numbers, hand):
    answer = ''
    pos = {
        1:(0,0), 2:(0,1), 3:(0,2),
        4:(1,0), 5:(1,1), 6:(1,2),
        7:(2,0), 8:(2,1), 9:(2,2),
        "*":(3,0), 0:(3,1), "#":(3,2)
    }
    
    left = "*"
    right = "#"
    
    for num in numbers:
        if num in [1,4,7]:
            answer += "L"
            left = num

        elif num in [3,6,9]:
            answer += "R"
            right = num
            
        else:
            left_dist = abs(pos[left][0] - pos[num][0]) + abs(pos[left][1] - pos[num][1])
            right_dist = abs(pos[right][0] - pos[num][0]) + abs(pos[right][1] - pos[num][1])

            if left_dist < right_dist:
                answer += "L"
                left = num

            elif left_dist > right_dist:
                answer += "R"
                right = num

            else:
                if hand == "left":
                    answer += "L"
                    left = num
                else:
                    answer += "R"
                    right = num

    return answer

## 풀이전략, 핵심 아이디어
# 좌표를 직접 저장해서 문제를 단순화하는 것이 핵심
# 키패드의 위치를 이용하여 abs(숫자차이)로 최단거리를 구하는 게 중요했던 문제
# abs() 부분 다시 풀어보기
