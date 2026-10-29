class Solution {
    public String solution(String my_string, String letter) {
        return my_string.replace(letter, "");
    }
}

## 풀이전략, 핵심 아이디어
# replace로 해당 문자 없애기
# StringBuilder로 푼다면
class Solution {
    public String solution(String my_string, String letter) {
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < my_string.length(); i++) {
            if (my_string.charAt(i) != letter.charAt(0)) {
                sb.append(my_string.charAt(i));
            }
        }

        return sb.toString();
    }
}  
