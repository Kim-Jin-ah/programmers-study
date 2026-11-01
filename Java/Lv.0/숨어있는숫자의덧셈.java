class Solution {
    public int solution(String my_string) {
        int answer = 0;
        for (int i=0; i<my_string.length(); i++) {
            char c = my_string.charAt(i);
            if (c>='0' && c<='9') {
                answer += c - '0';
            }
        }
        return answer;
    }
}

## 풀이전략, 핵심 아이디어
# 문자가 숫자인지 확인하고 문자 형태의 숫자를 정수로 변환.
# Character.isDigit()을 사용하는 방법도 있음. -> 해당 문자가 숫자인지 확인해주는 메서드
