import java.util.Arrays;
class Solution {
    public int solution(int[] sides) {
        Arrays.sort(sides);
        if (sides[2] < sides[0]+sides[1]) {return 1;}
        else {return 2;}
    }
}

// 풀이전략, 핵심 아이디어
// 배열 정렬로 가장 큰 수 찾은 후, 조건식으로 필터링
