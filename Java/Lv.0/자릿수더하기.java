class Solution {
    public int solution(int n) {
        int answer = 0;
        
        while (n > 0) {
            answer += n % 10;
            n /= 10;
        }
        return answer;
    }
}

## 풀이전략, 핵심 아이디어
# %10 으로 가장 마지막 자릿수 구하기
# /=10 으로 마지막 자릿수를 잘라냄 반복
