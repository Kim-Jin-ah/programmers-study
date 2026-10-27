class Solution {
    public int[] solution(int money) {
        int[] answer = new int[2];
        answer[0] = money / 5500;
        answer[1] = money % 5500;
        return answer;
    }
}

## 풀이전략, 핵심 아이디어
# 배열의 크기를 정해두고 0번째엔 몫, 1번째엔 나머지를 넣어서 반환
