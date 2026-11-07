class Solution {
    public long[] solution(int x, int n) {
        long[] answer = new long[n];
        
        for (int i=0; i<n; i++) {
            answer[i] = (long) x * (i+1);
        }
        return answer;
    }
}

## 풀이전략, 핵심 아이디어
# 반환 타입을 우선적으로 확인하고, 중간 계산 과정에서도 오버플로가 발생하지 않도록 주의
# 각 자료형에 맞추어 형변환 신경쓰기
