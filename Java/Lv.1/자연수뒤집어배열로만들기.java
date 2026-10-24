class Solution {
    public int[] solution(long n) {
        String s = String.valueOf(n);
        int[] answer = new int[s.length()];
        
        int idx = 0;
        while (n > 0) {
            answer[idx] = (int) (n % 10);
            n /= 10;
            idx++;
        }
        return answer;
    }
}

## 풀이전략, 핵심 아이디어
# s.length()로 배열의 크기를 정하고
# n % 10 과 n /= 10을 반복해 자릿수를 뒤집어 저장
