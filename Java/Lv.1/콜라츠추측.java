class Solution {
    public int solution(long num) {
        int count = 0;
        
        while (num != 1) {
            if (count >= 500) {return -1;}
            
            if (num % 2 == 0) {
                num /= 2;
            } else {
                num = (num*3) + 1;
            }
            count++;
        }      
        return count;
    }
}

// 풀이전략, 핵심 아이디어
// 반복 연산으로 값이 커질 가능성이 있다면 자료형의 범위를 고려해야함
// 따라서 int num이 아닌 long num으로 해야함
