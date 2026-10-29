class Solution {
    public int[] solution(int[] num_list) {
        int[] answer = new int[2];
        for (int i=0; i<num_list.length; i++) {
            if (num_list[i] % 2 == 0) {
                answer[0]++;
            } else {answer[1]++;}
        }
        return answer;
    }
}

## 풀이전략, 핵심 아이디어
# 결과를 저장할 배열을 먼저 만들어 놓은 후
# %2 == 0으로 짝수인지 판단하여 해당되는 answer의 인덱스에 +1
