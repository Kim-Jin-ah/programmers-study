import java.util.Arrays;
class Solution {
    public String solution(String s) {
        char[] arr = s.toCharArray();
        Arrays.sort(arr);
        
        return new StringBuilder(new String(arr)).reverse().toString();
    }
}

// 풀이전략, 핵심 아이디어
// Arrays.sort() -> 오름차순 + reverse() -> 내림차순으로 바꿈
