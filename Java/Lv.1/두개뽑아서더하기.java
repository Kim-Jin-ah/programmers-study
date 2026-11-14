import java.util.*;
class Solution {
    public int[] solution(int[] numbers) {
        HashSet<Integer> set = new HashSet<>();
        
        for (int i=0; i<numbers.length; i++) {
            for (int j=i+1; j<numbers.length; j++) {
                set.add(numbers[i]+numbers[j]);
            }
        }
        
        int[] answer = new int[set.size()];
        int index = 0;
        
        for (int num : set) {
            answer[index++] = num;
        }
        Arrays.sort(answer);
        
        return answer;
    }
}

// 풀이전략, 핵심 아이디어
// hashset을 사용하여 중복없이 저장 후 int[] answer에 넣어 반환
