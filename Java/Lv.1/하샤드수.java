class Solution {
    public boolean solution(int x) {
        int sum = 0;
        int num = x;
        
        while (num > 0) {
            sum += num % 10;
            num /= 10;
        }
        return x % sum == 0;
    }
}

## 풀이전략, 핵심 아이디어
# while문을 돌려 %10, /10 반복하며 값 누적
