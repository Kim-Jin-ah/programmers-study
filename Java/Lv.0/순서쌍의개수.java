class Solution {
    public int solution(int n) {
        int answer = 0;
        for (int i=1; i<= Math.sqrt(n); i++) {
            if (n % i == 0) {
                if (i*i == n) {
                    answer += 1;
                } else {answer += 2;}
            }
        }
        return answer;
    }
}

## 풀이전략, 핵심 아이디어
# 약수의 대칭성을 활용해 반복횟수 줄이기
