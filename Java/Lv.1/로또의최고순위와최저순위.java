class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int win = 0;
        int zero = 0;

        for (int i = 0; i < lottos.length; i++) {
            if (lottos[i] == 0) {
                zero++;
            } else {
                for (int j = 0; j < win_nums.length; j++) {
                    if (lottos[i] == win_nums[j]) {
                        win++;
                        break;
                    }
                }
            }
        }
        
        int max = win + zero;
        int min = win;

        int best = Math.min(7 - max, 6);
        int worst = Math.min(7 - min, 6);

        return new int[]{best, worst};
    }
}

// 풀이전략, 핵심 아이디아
// 0의 개수와 당첨번호와 일치하는 개수 구하는 것이 포인트
// 마지막에 등수 계산을 위해 min 사용한 것 주의
