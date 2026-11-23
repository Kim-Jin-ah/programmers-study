class Solution {
    public int solution(String[][] board, int h, int w) {
        int n = board.length;
        int count = 0;
        int[] dh = {0,1,-1,0};
        int[] dw = {1,0,0,-1};
        
        for (int i=0; i<4; i++) {
            int nh = h + dh[i];
            int nw = w + dw[i];
             if (nh >= 0 && nh < n && nw >= 0 && nw < n) {
                if (board[h][w].equals(board[nh][nw])) {
                    count++;
                }
            }
        }
        return count;
    }
}

// 풀이전략, 핵심 아이디어
// 기준 칸과 상하좌우에 있는 칸의 색이 같으면 개수 증가
