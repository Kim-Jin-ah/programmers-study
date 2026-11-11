import java.util.Arrays;
class Solution {
    public int solution(int[] d, int budget) {
        int answer = 0;
        Arrays.sort(d);
        
        for (int i=0; i<d.length; i++) {
            if (budget >= d[i]) {
                budget -= d[i];
                answer++;
            } else {break;}
        }
        return answer;
    }
}

// 풀이전략, 핵심 아이디어
// 배열을 오름차순으로 정렬한 뒤 현재 부서에 지원한 금액만큼 남은 예산 차감
