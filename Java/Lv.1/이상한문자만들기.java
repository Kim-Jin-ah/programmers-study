class Solution {
    public String solution(String s) {
        StringBuilder answer = new StringBuilder();
        int idx = 0;

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            if (c == ' ') {
                answer.append(' ');
                idx = 0;
            } else {
                if (idx % 2 == 0) {
                    answer.append(Character.toUpperCase(c));
                } else {
                    answer.append(Character.toLowerCase(c));
                }
                idx++;
            }
        }
        return answer.toString();
    }
}

// 풀이전략, 핵심 아이디어
// '' 와 "" 구분 헷갈리지 않기
// StringBuilder를 사용하여 성능 최적화
