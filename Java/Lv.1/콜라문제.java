class Solution {
    public int solution(int a, int b, int n) {
        int answer = 0;
        while (n >= a) {
            answer += (n/a)*b;
            n = (n/a)*b + (n%a);
        }
        return answer;
    }
}

// 풀이전략, 핵심 아이디어
// 반복 조건은 최소한 a개 이상의 빈 병이 있어야 하므로 n >= a로 설정해야함 -> 주의!
// 새로 받는 콜라 계산, 빈 병 재고 갱신 
