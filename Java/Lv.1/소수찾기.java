class Solution {
    public int solution(int n) {
        int answer = 0;
        boolean[] isPrime = new boolean[n+1];
        
        for (int i=2; i<=n; i++) {
            isPrime[i] = true;
        }
        
        for (int i=2; i*i<=n; i++) {
            if (isPrime[i]) {
                for (int j=i*i; j<=n; j+=i) {
                    isPrime[j] = false;
                }
            }
        }
        
        for (int i=2; i<=n; i++) {
            if (isPrime[i]) {
                answer++;
            }
        }
        return answer;
    }
}

// 풀이전략, 핵심 아이디어
// 배수를 지우면서 소수가 아닌 수를 걸러냄
// 과정 기억하기
