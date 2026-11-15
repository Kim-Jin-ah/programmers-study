import java.util.*;
class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];

        for (int idx = 0; idx < commands.length; idx++) {
            int i = commands[idx][0];
            int j = commands[idx][1];
            int k = commands[idx][2];
            
            int[] sliced = Arrays.copyOfRange(array,i-1,j);
            Arrays.sort(sliced);
            answer[idx] = sliced[k-1];
        }
        return answer;
    }
}

// 풀이전략, 핵심 아이디어
// Arrays.copyOfRange()로 배열 잘라낸 후, 정렬 + 인덱스 보정
