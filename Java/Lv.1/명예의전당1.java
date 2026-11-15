import java.util.PriorityQueue;
class Solution {
    public int[] solution(int k, int[] score) {
        int[] answer = new int[score.length];
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        
        for (int i=0; i<score.length; i++) {
            pq.add(score[i]);
            
            if (pq.size() > k) {
                pq.poll();
            }
            
            answer[i] = pq.peek();
        }
        return answer;
    }
}

// 풀이전략, 핵심 아이디어
// 최소힙을 사용하여 각 구간에서의 가장 낮은 점수 가져오기 가 핵심
