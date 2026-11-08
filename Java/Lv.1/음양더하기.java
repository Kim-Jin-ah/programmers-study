class Solution {
    public int solution(int[] absolutes, boolean[] signs) {
        int answer = 0;
        for (int i=0; i<absolutes.length; i++) {
            if (signs[i]) {answer += absolutes[i];}
            else {answer -= absolutes[i];}
        }
        return answer;
    }
}

// 풀이전략, 핵심 아이디어
// 두 배열의 인덱스가 서로 대응함을 활용하여 덧셈 또는 뺄셈 적용
// 삼항 연산자를 사용한다면
class Solution {
    public int solution(int[] absolutes, boolean[] signs) {
        int sum = 0;

        for (int i = 0; i < absolutes.length; i++) {
            sum += signs[i] ? absolutes[i] : -absolutes[i];
        }

        return sum;
    }
}
