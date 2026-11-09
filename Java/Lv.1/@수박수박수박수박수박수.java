class Solution {
    public String solution(int n) {
        String answer = "";
        for (int i=0; i<n; i++) {
            if (i % 2 == 0) {
                answer += "수";
            } else {
                answer += "박";
            }
        }
        return answer;
    }
}

// 풀이전략, 핵심 아이디어
// n번까지 반복문을 돌려
// 홀수 인덱스와 짝수 인덱스를 판별 후 각각에 맞는 글자 추가시키기 
