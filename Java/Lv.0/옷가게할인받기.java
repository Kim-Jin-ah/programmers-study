class Solution {
    public int solution(int price) {
        int answer = 0;
        
        if (price >= 500000) {
            answer = (int) (price * 0.8);
        } else if (price >= 300000) {
            answer = (int) (price * 0.9);
        } else if (price >= 100000) {
            answer = (int) (price * 0.95);
        } else {
            answer = price;
        }
        
        return answer;
    }
}

## 풀이전략, 핵심 아이디어
# (int)를 사용해 정수로 반환하여 출력
# 조건이 큰 금액부터 검사하는 것이 중요
