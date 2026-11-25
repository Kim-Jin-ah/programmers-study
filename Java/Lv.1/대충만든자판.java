import java.util.HashMap;
class Solution {
    public int[] solution(String[] keymap, String[] targets) {
        int[] answer = new int[targets.length];
        HashMap<Character,Integer> map = new HashMap<>();
        
        for (String alpha : keymap) {
            for (int i=0; i<alpha.length(); i++) {
                char c = alpha.charAt(i);
                
                if (!map.containsKey(c) || map.get(c) > i+1) {
                    map.put(c, i+1);
                }
            }
        }
        
        for (int j=0; j<targets.length; j++) {
            String target = targets[j];
            
            for (int i=0; i<target.length(); i++) {
                char c = target.charAt(i);
                
                if (!map.containsKey(c)) {
                    answer[j] = -1;
                    break;
                }
                
                answer[j] += map.getOrDefault(c,0);
            }
        }
        return answer;
    }
}

// 풀이전략, 핵심 아이디어
// HashMap을 사용하여 순서 찾기
// 대소문자 입력 신경쓰고 HashMap 문법 더 익혀야함
