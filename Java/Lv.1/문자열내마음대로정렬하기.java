import java.util.Arrays;
class Solution {
    public String[] solution(String[] strings, int n) {
        String[] answer = {};
        Arrays.sort(strings,(s1,s2) -> {
            if (s1.charAt(n) != s2.charAt(n)) {
                return s1.charAt(n) - s2.charAt(n);
            }
            return s1.compareTo(s2);
        });
        return strings;
    }
}

// 풀이전략, 핵심 아이디어
// Comparator를 활용하여 배열 정렬
