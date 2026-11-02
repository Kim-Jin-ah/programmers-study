class Solution {
    public String solution(String my_string) {
        String answer = "";
        for (int i=0; i<my_string.length(); i++) {
            char c = my_string.charAt(i);
            
            if (Character.isUpperCase(c)) {
                answer += Character.toLowerCase(c);
            } else {
                answer += Character.toUpperCase(c);
            }
        }
        return answer;
    }
}

## 풀이전략, 핵심 아이디어
# Character 클래스의 메서드를 이용해 대소문자 구분 및 변환
# ASCII 코드를 활용하는 방법으로는
class Solution {
    public String solution(String my_string) {
        String answer = "";

        for (int i = 0; i < my_string.length(); i++) {
            char c = my_string.charAt(i);

            if (c >= 'a' && c <= 'z') {
                answer += (char)(c - 32);
            } else {
                answer += (char)(c + 32);
            }
        }

        return answer;
    }
}
# 영어 알파벳의 대소문자 코드 차이가 32인 사실 활용
