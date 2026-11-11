import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        List<Integer> list = new ArrayList<>();
        
        for (int i=0; i<arr.length; i++) {
            if (i == 0 || arr[i-1] != arr[i]) {
                list.add(arr[i]);
            }
        }
        
        int[] answer = new int[list.size()];

        for (int i=0; i<list.size(); i++) {
            answer[i] = list.get(i);
        }
        return answer;
    }
}

// 풀이전략, 핵심 아이디어
// Arraylist를 생성하여 첫 번째 숫자는 무조건 저장, 이전 숫자와 현재 숫자가 다르면 저장 조건을 넣어 필터링
// 그 후 int[] 배열에 넣기
