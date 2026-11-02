class Solution {
    public int[] solution(int n) {
        int count = 0;
        for (int i=1; i<=n; i++) {
            if (n % i == 0) {
                count++;
            }
        }
        int [] answer = new int[count];
        int index = 0;
        for (int i=1; i<=n; i++) {
            if (n % i == 0) {
                answer[index] = i;
                index++;
            }
        }
        return answer;
    }
}

# 또는 Arraylist를 사용하여
import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] solution(int n) {
        List<Integer> list = new ArrayList<>();
        
        // 1부터 n까지 나누어떨어지는지 확인
        for (int i = 1; i <= n; i++) {
            if (n % i == 0) {
                list.add(i); // 나누어떨어지면 약수이므로 리스트에 추가
            }
        }
        
        // List를 int[] 배열로 변환
        int[] answer = new int[list.size()];
        for (int i = 0; i < list.size(); i++) {
            answer[i] = list.get(i);
        }
        
        return answer;
    }
}
