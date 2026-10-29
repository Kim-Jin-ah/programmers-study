class Solution {
    public String solution(String my_string) {
        String answer = "";
        for (int i= my_string.length()-1; i>=0; i--) {
            answer += my_string.charAt(i);
        }
        return answer;
    }
}

## 풀이전략, 핵심 아이디어
# 반복문으로 뒤에서부터 가져와 charAt(i)를 이용해 문자로 가져오기
# StringBuilder의 reverse() 메서드를 활용하면
class Solution {
    public String solution(String my_string) {
        return new StringBuilder(my_string).reverse().toString();
    }
}
