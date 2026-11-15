class Solution {
    public int solution(String s) {
        String[] words = {"zero","one","two","three","four","five","six","seven","eight","nine"};
        
        for (int i=0; i<words.length; i++) {
            s = s.replace(words[i], String.valueOf(i));
        }
        return Integer.parseInt(s);
    }
}

// 풀이전략, 핵심 아이디어
// 0부터 9까지 words를 순회하면서, 문자열 안의 모든 영단어들을 replace
