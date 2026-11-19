import java.util.Arrays;
class Solution {
    public int solution(int k, int m, int[] score) {
        int answer = 0;
        Arrays.sort(score);
        int start = score.length % m;
        
        for (int i=start; i<score.length; i+=m) {
            answer += score[i] * m;
        }
        return answer;
    }
}

// 풀이전략, 핵심 아이디어
// 오름차순 정렬, 나머지로 남는 사과를 먼저 제외시킨 후 그 인덱스부터 반복문으로 접근
