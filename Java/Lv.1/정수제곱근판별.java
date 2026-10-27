class Solution {
    public long solution(long n) {
        long i = (long) Math.sqrt(n);
            if (i*i == n) {
                return (i+1)*(i+1);
            } else {return -1;}
    }
}

## 풀이전략, 핵심 아이디어
# Math.sqrt(n)으로 n의 제곱근을 구하고 결과값은 double이므로 long으로 바꿔주기
# 삼항 연산자로 바꾸면
class Solution {
    public long solution(long n) {
        long sqrt = (long) Math.sqrt(n);
        return sqrt * sqrt == n ? (sqrt + 1) * (sqrt + 1) : -1;
    }
}
