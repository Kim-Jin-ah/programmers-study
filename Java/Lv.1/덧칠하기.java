class Solution {
    public int solution(int n, int m, int[] section) {
        int answer = 0;
        int lastpaint = 0;
        
        for (int s : section) {
            if (s > lastpaint) {
                answer++;
                lastpaint = s + m - 1;
            }
        }
        return answer;
    }
}

// 풀이전략, 핵심 아이디어
// 페인트 칠한 구역의 끝 번호를 저장하는 변수 만들고
// 페인트칠이 필요한 구역인지 확인 후 이미 칠했는지 확인
