import java.util.*;
class Solution {
    public int[] solution(int N, int[] stages) {
        int[] answer = new int[N];
        int[] count = new int[N+2];
        for (int s : stages) {
            count[s]++;
        }
        
        int total = stages.length;
        double[] failure = new double[N+1];
        
        for (int i=1; i<=N; i++) {
            if (total == 0) {failure[i] = 0;}
            else {failure[i] = (double) count[i] / total;}
            total -= count[i];
        }
        
        Integer[] arr = new Integer[N];
        for (int i=0; i<N; i++) {
            arr[i] = i + 1;
        }
        Arrays.sort(arr,(a,b) -> Double.compare(failure[b],failure[a]));
        
        for (int i=0; i<N; i++) {
            answer[i] = arr[i];
        }
        
        return answer;
    }
}

// 풀이전략, 핵심 아이디어
// 각 스테이지에 도전 중인 사람 수를 센 후 실패율 계산
// 실패율 기준 내림차순 정렬(람다식을 써야하므로 Integer[] 만들어주기)
