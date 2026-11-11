class Solution {
    public int[] solution(int n, int m) {
        int a = n;
        int b = m;
        
        while (b!=0) {
            int temp = a % b;
            a = b;
            b = temp;
        }
        
        int gcd = a;
        int lcm = (n*m) / gcd;
        
        return new int[]{gcd,lcm};
    }
}

// 풀이전략, 핵심 아이디어
// 유클리드 호제법으로 최대공약수를 찾은 후 최소공배수 구하기
