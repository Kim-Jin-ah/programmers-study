class Solution {
    public long solution(int a, int b) {
        long answer = 0;
        for (int i = Math.min(a,b); i <= Math.max(a,b); i++) {
            answer += i;
        }
        return answer;
    }
}

## 풀이전략, 핵심 아이디어
# Math.min() / Math.max() => 두 값 중 작은 값과 큰 값 찾기
# for문을 사용해 누적합계 구하기
