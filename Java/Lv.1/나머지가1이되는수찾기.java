class Solution {
    public int solution(int n) {
        int answer = 0;
        for (int i=2; i<n; i++) {
            if (n % i == 1) {
                return i;
            }
        }
        return 0;
    }
}

## 풀이전략, 핵심 아이디어
# 조건에 만족하면 바로 return. return 0도 잊지말기
