class Solution {
    public String solution(String s, int n) {
        StringBuilder answer = new StringBuilder();
        
        for (int i=0; i<s.length(); i++) {
            char c = s.charAt(i);
            
            if (c == ' ') {
                answer.append(' ');
            } else if (c >= 'A' && c <= 'Z') {
                char shifted = (char) ((c-'A'+n) % 26 + 'A');
                answer.append(shifted);
            } else if (c >= 'a' && c <= 'z') {
                char shifted = (char) ((c-'a'+n) % 26 + 'a');
                answer.append(shifted);
            }
        }
        return answer.toString();
    }
}

// 풀이전략, 핵심 아이디어
// 대문자인 경우와 소문자인 경우를 나누어
// 'A' 또는 'a'를 0으로 기준잡고 n을 더한 뒤, 알파벳 개수인 26으로 나눈 나머지 계산
