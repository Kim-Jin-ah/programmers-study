class Solution {
    public int solution(String[] babbling) {
        int answer = 0;

        for (String s : babbling) {
            if (s.contains("ayaaya") ||
                s.contains("yeye") ||
                s.contains("woowoo") ||
                s.contains("mama")) {
                continue;
            }

            s = s.replace("aya", " ");
            s = s.replace("ye", " ");
            s = s.replace("woo", " ");
            s = s.replace("ma", " ");

            if (s.trim().isEmpty()) {
                answer++;
            }
        }
        return answer;
    }
}

// 풀이전략, 핵심 아이디어
// 같은 발음을 연속해서 두 번 사용하는 경우 걸러냄
// replace(), isEmpty() 활용
