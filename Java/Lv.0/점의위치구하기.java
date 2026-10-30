class Solution {
    public int solution(int[] dot) {
        int x = dot[0];
        int y = dot[1];

        if (x > 0 && y > 0) {
            return 1;
        } else if (x < 0 && y > 0) {
            return 2;
        } else if (x < 0 && y < 0) {
            return 3;
        } else {
            return 4;
        }
    }
}

## 풀이전략, 핵심 아이디어
# dot의 0번째 인덱스와 1번째 인덱스를 각각 변수에 넣고
# 그 값을 가지고 비교 실행
# 삼항 연산자를 쓴다면
class Solution {
    public int solution(int[] dot) {
        if (dot[0] > 0) {
            return dot[1] > 0 ? 1 : 4;
        } else {
            return dot[1] > 0 ? 2 : 3;
        }
    }
}
