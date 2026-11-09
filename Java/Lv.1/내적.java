class Solution {
    public int solution(int[] a, int[] b) {
        int answer = 0;
        for (int i=0; i<a.length; i++) {
            answer += a[i] * b[i];
        }
        return answer;
    }
}

// 풀이전략, 핵심 아이디어
// a,b 모두 같은 인덱스에 위치한 것을 곱함을 활용
