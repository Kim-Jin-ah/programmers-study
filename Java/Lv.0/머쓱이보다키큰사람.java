import java.util.Arrays;
class Solution {
    public int solution(int[] array, int height) {
        Arrays.sort(array);
        int answer = 0;
        for (int i=0; i<array.length; i++) {
            if (array[i] > height) {
                answer += 1;
            }
        }
        return answer;
    }
}

## 풀이전략, 핵심 아이디어
# 반복문을 통해 조건에 맞으면 answer += 1
