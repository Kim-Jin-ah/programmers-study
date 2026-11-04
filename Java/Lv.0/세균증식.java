class Solution {
    public int solution(int n, int t) {
        return (int) (n * Math.pow(2, t));
    }
}
# 거듭제곱으로 푸는 방법 또는

class Solution {
    public int solution(int n, int t) {
        int answer = n;

        for (int i = 0; i < t; i++) {
            answer *= 2;
        }

        return answer;
    }
}
# 반복문을 통해 푸는 방법
# 어떤 방법이든 문제 이해만 잘 하면 바로 풀 수 있음
