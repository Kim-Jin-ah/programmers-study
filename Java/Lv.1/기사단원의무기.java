class Solution {
    public int solution(int number, int limit, int power) {
        int answer = 0;
        for (int i=1; i<=number; i++) {
            int count = 0;
            for (int j=1; j<=i; j++) {
                if (i % j == 0) {
                    count++;
                }
            }
            if (count > limit) {
                answer += power;
            } else {answer += count;}
        }
        return answer;
    }
}
// 이 방법보다
class Solution {
    public int solution(int number, int limit, int power) {
        int totalWeight = 0;

        for (int i = 1; i <= number; i++) {
            int divisors = countDivisors(i);

            if (divisors > limit) {
                totalWeight += power;
            } else {
                totalWeight += divisors;
            }
        }
        
        return totalWeight;
    }

    private int countDivisors(int n) {
        int count = 0;
        
        for (int i = 1; i * i <= n; i++) {
            if (i * i == n) {
                count++;
            } else if (n % i == 0) {
                count += 2;
            }
        }
        return count;
    }
}
// 이렇게 푸는 게 더 최적화된 방법
// 제곱근 사용하는 방법 익히기
