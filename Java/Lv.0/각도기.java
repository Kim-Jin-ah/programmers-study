class Solution {
    public int solution(int angle) {
        
        if (angle < 90) {return 1;}
        else if (angle == 90) {return 2;}
        else if (angle < 180) {return 3;}
        else {return 4;}
        
    }
}

## 풀이전략, 핵심 아이디어
# 파이썬과 다르게 자바에선 elif가 아닌 else if임을 기억하기
