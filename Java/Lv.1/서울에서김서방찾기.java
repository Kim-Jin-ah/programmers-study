class Solution {
    public String solution(String[] seoul) {
        String answer = "";
        for (int i=0; i<seoul.length; i++) {
            if (seoul[i].equals("Kim")) {
                return "김서방은 " + i + "에 있다";
            }
        }
        return "";
    }
}

// 풀이전략, 핵심 아이디어
// equals로 문자열의 실제 내용을 비교 후
// +를 사용해 정수와 문자열 연결
