class Solution {
    public int solution(String s) {
        int answer = 0;
        char x = 0;
        int xcount = 0;
        int othercount = 0;
        
        for (int i=0; i<s.length(); i++) {
            char current = s.charAt(i);
            
            if (xcount == 0 && othercount == 0) {
                x = current;
            }
            
            if (current == x) {xcount++;}
            else {othercount++;}

            if (xcount == othercount) {
                answer++;
                xcount = 0;
                othercount = 0;
            }
        }
        
        if (xcount != 0 || othercount != 0) {
            answer++;
        }
        
        return answer;
    }
}

// 풀이전략, 핵심 아이디어
// 카운터 초기화로 구간 분리 표현
// 남은 꼬리 문자열 처리
// char 비교엔 == 사용. equals 필요없음 주의
