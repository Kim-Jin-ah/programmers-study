import java.util.Arrays;

class Solution {
    public long solution(long n) {
        char [] list = String.valueOf(n).toCharArray();
        
        Arrays.sort(list);
        
        StringBuilder sb = new StringBuilder(new String(list));
        sb.reverse();
        
        return Long.parseLong(sb.toString());
    }
}

## 풀이전략, 핵심 아이디어
# 정수 n을 문자열로 바꾼뒤 문자를 담은 배열 만들고
# 오름차순 후 StringBuilder에 넣어 reverse() 한 후
# 내림차순 된 문자열을 long 타입의 숫자로 변환하여 반환
