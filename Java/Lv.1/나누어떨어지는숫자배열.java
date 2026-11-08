import java.util.Arrays;
class Solution {
    public int[] solution(int[] arr, int divisor) {
        int[] answer = Arrays.stream(arr)
                             .filter(n -> n % divisor == 0)
                             .sorted()
                             .toArray();
        if (answer.length == 0) {
            return new int[]{-1};
        }
        return answer;
    }
}

// 풀이전략, 핵심 아이디어
// Arrays의 Stream 문법을 사용하여 필터링 및 오름차순
