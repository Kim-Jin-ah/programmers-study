class Solution {
    public int solution(String[] s1, String[] s2) {
        int answer = 0;
        for (int i=0; i<s1.length; i++) {
            
            for (int j=0; j<s2.length; j++) {
                if (s1[i].equals(s2[j])) {
                    answer++;
                }
            }
        }
        return answer;
    }
}

// 풀이전략, 핵심 아이디어
// 문자열을 비교할 때 == 가 아니라 .equals() 사용 기억하기
