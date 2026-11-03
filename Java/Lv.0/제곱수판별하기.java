class Solution {
    public int solution(int n) {
        double sqrt = Math.sqrt(n);
        
        return (sqrt == (int) sqrt) ? 1 : 2;
    }
}

## 풀이전략, 핵심 아이디어
# 제곱근을 구한 뒤, 그 제곱근을 정수로 바꿨을 때 원래 값과 일치하는지 비교
