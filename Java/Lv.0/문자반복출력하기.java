class Solution {
    public String solution(String my_string, int n) {
        String answer = "";
        for (int i=0; i<my_string.length(); i++) {
            for (int j=0; j<n; j++) {
                answer += my_string.charAt(i);
            }
        }
        return answer;
    }
}

## 풀이전략, 핵심 아이디어
# 중첩반복문으로 각 문자를 정해진 횟수만큼 반복하기
# StringBuilder를 사용한다면
class Solution {
    public String solution(String my_string, int n) {
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < my_string.length(); i++) {
            for (int j = 0; j < n; j++) {
                sb.append(my_string.charAt(i));
            }
        }

        return sb.toString();
    }
}
