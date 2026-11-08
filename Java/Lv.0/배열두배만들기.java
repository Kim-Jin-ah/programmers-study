class Solution {
    public int[] solution(int[] numbers) {
        int[] answer = new int[numbers.length];
        for (int i=0; i<numbers.length; i++) {
            answer[i] = numbers[i]*2;
        }
        return answer;
    }
}

// 풀이전략, 핵심 아이디아
// 배열의 크기를 넣은 answer에 반복문을 돌려 *2한 값을 차례대로 넣기
