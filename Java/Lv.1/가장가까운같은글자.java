import java.util.Arrays;
class Solution {
    public int[] solution(String s) {
        int[] answer = new int[s.length()];
        int[] lastSeen = new int[26];
        Arrays.fill(lastSeen,-1);
        
        for (int i=0; i<s.length(); i++) {
            char c = s.charAt(i);
            int idx = c - 'a';
            
            if (lastSeen[idx] == -1) {
                answer[i] = -1;
            } else {
                answer[i] = i - lastSeen[idx];
            }
            
            lastSeen[idx] = i;
        }
        return answer;
    }
}

// 풀이전략, 핵심 아이디어
// lastSeen 배열을 -1로 초기화
// c - 'a'로 아스키코드 활용법을 사용
// 거리 계산과 인덱스 갱신
