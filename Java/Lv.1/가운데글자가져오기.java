class Solution {
    public String solution(String s) {
        int length = s.length();
        
        if (s.length() % 2 == 0) {
            return s.substring(length/2 - 1, length/2 + 1);
        } else {
            return s.substring(length/2, length/2 + 1);
        }
    }
}

// 풀이전략, 핵심 아이디어
// str.substring(시작인덱스, 끝 인덱스+1) 활용
