import java.util.ArrayList;
import java.util.List;
class Solution {
    public int[] solution(int n) {
        List<Integer> list = new ArrayList<>();
        for (int i=1; i<=n; i++) {
            if (i % 2 != 0) {
                list.add(i);
            }
        }
        
        int[] answer = new int[list.size()];
        for (int i=0; i<list.size(); i++) {
            answer[i] = list.get(i);
        }
        return answer;
    }
}

## 풀이전략, 핵심 아이디어
# ArrayList를 사용하여 홀수인지 확인한 숫자들을 넣고, answer 배열에 다시 넣기
# 또는 배열 크기를 미리 계산하여 푸는 방법으로
  class Solution {
    public int[] solution(int n) {
        int[] answer = new int[(n + 1) / 2];

        for (int i = 0; i < answer.length; i++) {
            answer[i] = 2 * i + 1;
        }

        return answer;
    }
}
