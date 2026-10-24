public class Solution {
    public int solution(int n) {
        int answer = 0;
      
        while (n>0) {
            answer += n % 10;
            n /= 10;
        }
        return answer;
    }
}

## 풀이전략, 핵심 아이디어
# n이 0보다 클 동안 n을 10으로 나눈 나머지(마지막자릿수) 누적하고 n을 10으로 나누어 마지막 자릿수 제거

# 문자열 변환 방식으로 푼다면
public class Solution {
    public int solution(int n) {
        int answer = 0;
        String str = String.valueOf(n);

        for (int i = 0; i < str.length(); i++) {
            answer += str.charAt(i) - '0';
        }
        
        return answer;
    }
}  
