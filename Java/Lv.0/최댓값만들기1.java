import java.util.Arrays;
class Solution {
    public int solution(int[] numbers) {
        Arrays.sort(numbers);
        int length = numbers.length;
        return numbers[length-1]*numbers[length-2];
    }
}

## 풀이전략, 핵심 아이디어
# array를 사용하여 sort()로 오름차순으로 변경하고
# 최댓값 만들 두 요소 곱하기
