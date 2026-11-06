class Solution {
    public int solution(int a, int b) {
        int num1 = Integer.parseInt("" + a + b);
        int num2 = 2 * a * b;
        return Math.max(num1,num2);
    }
}

## 풀이전략, 핵심 아이디어
# 빈 문자열을 먼저 더하여 숫자를 문자열로 변환 후
# int로 바꾸어 최대 비교
