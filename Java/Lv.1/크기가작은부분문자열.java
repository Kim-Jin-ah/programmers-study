class Solution {
    public int solution(String t, String p) {
        int answer = 0;
        int len = t.length() - p.length();
        
        for (int i=0; i<=len; i++) {
            String sub = t.substring(i,i+(p.length()));
            if (Long.parseLong(sub) <= Long.parseLong(p)) {
                answer++;
            }
        }
        return answer;
    }
}

// 풀이전략, 핵심 아이디어
// substring()으로 부분 문자열 추출
// Long.parseLong()으로 숫자로 변환
