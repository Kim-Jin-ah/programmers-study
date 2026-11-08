class Solution {
    public int solution(int[] numbers) {
        int sum = 45;
        
        for (int num : numbers) {
            sum -= num;
        }
        return sum;
    }
}

## 풀이전략, 핵심 아이디어
# 전체 합에서 배열에 들어있는 숫자 하나씩 뺴기
# Stream을 활용한다면
import java.util.Arrays;
class Solution {
    public int solution(int[] numbers) {
        return 45 - Arrays.stream(numbers).sum();
    }
}
