class Solution {
    public int[] solution(int[] numbers, int num1, int num2) {
        int[] answer = new int[num2-num1+1];
        for (int i=num1; i <= num2; i++) {
            answer[i-num1] = numbers[i];
        }
        return answer;
    }
}

## 풀이전략, 핵심 아이디어
# 반복문에서 num1부터 num2까지, 배열의 인덱스를 활용해 넣기
