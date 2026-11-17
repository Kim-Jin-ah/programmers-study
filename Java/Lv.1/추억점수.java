import java.util.HashMap;
class Solution {
    public int[] solution(String[] name, int[] yearning, String[][] photo) {
        int[] answer = new int[photo.length];
        HashMap<String,Integer> map = new HashMap<>();
        for (int i=0; i<name.length; i++) {
            map.put(name[i],yearning[i]);
        }
        
        for (int i=0; i<photo.length; i++) {
            int score = 0;
            for (String person : photo[i]) {
                score += map.getOrDefault(person,0);
            }
            answer[i] = score;
        }
        return answer;
    }
}

// 풀이전략, 핵심 아이디어
// HashMap을 사용하여 이름을 키로, 점수를 값으로 매칭하여 풀이
