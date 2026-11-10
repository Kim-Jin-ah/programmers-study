class Solution {
    public long solution(int price, int money, int count) {
        long answer = 0;
        
        for (int i=1; i<=count; i++) {
            answer += price * i;
        }
        if (answer > money) {return answer-money;}
        else {return 0;}
        
    }
}

// 풀이전략, 핵심 아이디어
// count까지 반복문을 통해 금액을 누적시키고
// 조건에 맞는지 확인 후 return값 반환
