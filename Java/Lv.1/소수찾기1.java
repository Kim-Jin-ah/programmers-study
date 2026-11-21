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
// isPrime 방법

class Solution {
    public int solution(int n) {
        boolean[] isComposite = new boolean[n + 1];

        isComposite[0] = true;
        isComposite[1] = true;

        for (int i = 2; i * i <= n; i++) {
            if (!isComposite[i]) {
                for (int j = i * i; j <= n; j += i) {
                    isComposite[j] = true;
                }
            }
        }

        int count = 0;
        for (int i = 2; i <= n; i++) {
            if (!isComposite[i]) {
                count++;
            }
        }
        return count;
    }
}
// isComposite 방법
