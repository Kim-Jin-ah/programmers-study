import java.util.ArrayList;
import java.util.List;
class Solution {
    public int[] solution(int n, int[] numlist) {
        List<Integer> list = new ArrayList<>();
        for (int i=0; i<numlist.length; i++) {
            if (numlist[i] % n == 0) {
                list.add(numlist[i]);
            }
        }
        
        int[] answer = new int[list.size()];
        for (int i = 0; i < list.size(); i++) {
            answer[i] = list.get(i);
        }
        return answer;
    }
}

## 풀이전략, 핵심 아이디어
# 크기가 가변적인 ArrayList에 먼저 담아둔 뒤 일반 배열 int[]로 변환
# 향상된 for문 형태( for (int num : numlist) ) 도 사용해보기
