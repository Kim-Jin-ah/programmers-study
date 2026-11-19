class Solution {
    public int solution(int[] wallet, int[] bill) {
        int answer = 0;
        
        while (true) {
            if ((bill[0] <= wallet[0] && bill[1] <= wallet[1]) || (bill[0] <= wallet[1] && bill[1] <= wallet[0])) {break;}
            
            if (bill[0] > bill[1]) {
                bill[0] /= 2;
            } else {
                bill[1] /= 2;
            }
            answer++;
        }
        return answer;
    }
}

// 풀이전략, 핵심 아이디어
// 가로와 세로의 방향이 바뀌어도 들어갈 수 있다는 것이 핵심
// 항상 긴 변을 접는다 주의하기
