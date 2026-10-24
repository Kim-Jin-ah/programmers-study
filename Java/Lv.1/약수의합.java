class Solution {
    public int solution(int n) {
        int answer = 0;
        for (int i = 1; i <= n; i++) {
            if (n % i == 0) {
                answer += i;
            }
        }
        return answer;
    }
}

## 풀이전략, 핵심 아이디어
# i를 1~n까지 순회하며 나누어 떨어지면 answer에 누적해서 더하기
