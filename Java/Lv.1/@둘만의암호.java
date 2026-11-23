class Solution {
    public String solution(String s, String skip, int index) {
        String answer = "";
        for (int i=0; i<s.length(); i++) {
            char c = s.charAt(i);
            int count = 0;
            
            while(count < index) {
                c++;
                if (c > 'z') {
                    c = 'a';
                }
                if (!skip.contains(String.valueOf(c))) {
                    count++;
                }
            }
            answer += c;
        }
        return answer;
    }
}

// 풀이전략, 핵심 아이디어
// stringbuilder로도 풀어보기
class Solution {
    public String solution(String s, String skip, int index) {
        boolean[] isSkipped = new boolean[26];
        for (int i = 0; i < skip.length(); i++) {
            isSkipped[skip.charAt(i) - 'a'] = true;
        }

        StringBuilder answer = new StringBuilder();

        for (int i = 0; i < s.length(); i++) {
            char current = s.charAt(i);
            int moved = 0;

            while (moved < index) {
                current = (char) ((current - 'a' + 1) % 26 + 'a');
                if (!isSkipped[current - 'a']) {
                    moved++;
                }
            }
            answer.append(current);
        }
        return answer.toString();
    }
}
