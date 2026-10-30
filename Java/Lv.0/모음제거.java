class Solution {
    public String solution(String my_string) {
        String answer = "";
        for (int i=0; i<my_string.length(); i++) {
            char c = my_string.charAt(i);
            
            if (c != 'a' && c != 'e' && c != 'i'
                && c != 'o' && c != 'u') {
                answer += c;
            }
        }
        return answer;
    }
}

## 풀이전략, 핵심 아이디어
# 문자열의 모든 문자를 반복문을 돌며 확인하고
# 모음이 아닌 경우에만 빈 문자열 answer에 추가하기
