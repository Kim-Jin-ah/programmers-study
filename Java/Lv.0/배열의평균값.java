class Solution {
    public double solution(int[] numbers) {
        double answer = 0;
        for (int i=0; i<numbers.length; i++) {
            answer += numbers[i];
        }
        return answer / numbers.length;
    }
}

## 풀이전략, 핵심 아이디어
# return 뒤에 오는 값의 자료형이 메서드의 반환 자료형과 호환되어야함 기억하기
