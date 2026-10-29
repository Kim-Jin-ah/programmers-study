class Solution {
    public int solution(int n) {
        int answer = 0;
        for (int i=2; i<=n; i++) {
            if (i % 2 ==0) {
                answer += i;
            }
        }
        return answer;
    }
}

## 풀이전략, 핵심 아이디어
# 나머지가 0인지 아닌지 판단해 홀수와 짝수 판단한 후
# 해당되면 answer에 더하기
