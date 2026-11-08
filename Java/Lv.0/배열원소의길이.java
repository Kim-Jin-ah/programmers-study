class Solution {
    public int[] solution(String[] strlist) {
        int[] answer = new int[strlist.length];
        for (int i=0; i<strlist.length; i++) {
            answer[i] = strlist[i].length();
        }
        return answer;
    }
}

// 풀이전략, 핵심 아이디어
// length, length()의 차이점 구분할 수 있어야함
