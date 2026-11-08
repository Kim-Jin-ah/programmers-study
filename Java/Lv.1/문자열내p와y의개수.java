class Solution {
    boolean solution(String s) {
        s = s.toLowerCase();
        int p = 0;
        int y = 0;

        for (int i=0; i<s.length(); i++) {
            if (s.charAt(i) == 'p') {p++;}
            else if (s.charAt(i) == 'y') {y++;}
        }
        return p == y;
    }
}

// 풀이전략, 핵심 아이디어
// s를 소문자로 변환한 후 문자열을 순회하면서 개수 세기
