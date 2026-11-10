class Solution {
    public int solution(int left, int right) {
        int answer = 0;
        for (int i=left; i<=right; i++) {
            int count = 0;
            for (int j=1; j<=i; j++) {
                if (i % j == 0) {
                    count++;
                }
            }
            if (count % 2 == 0) {
                answer += i;
            } else {answer -= i;}
        }
        return answer;
    }
}

// 풀이전략, 핵심 아이디어
// 이중 반복문 구조를 사용하여 안쪽 반복문에서 각 숫자의 약수를 찾을 수 있도록

// 다른 방법으로는 완벽한 제곱수만 약수가 홀수개라는 성질을 이용해
// Math.sqrt 사용한 방법
class Solution {
    public int solution(int left, int right) {
        int answer = 0;
      
        for (int i = left; i <= right; i++) {
            double sqrt = Math.sqrt(i);
            
            if (sqrt == (int) sqrt) {
                answer -= i;
            } else {
                answer += i;
            }
        }
        return answer;
    }
}
