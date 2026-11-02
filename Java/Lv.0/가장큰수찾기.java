class Solution {
    public int[] solution(int[] array) {
        int max = array[0];
        int index = 0;
        
        for (int i=0; i<array.length; i++) {
            if (array[i] > max) {
                max = array[i];
                index = i;
            }
        }
        return new int[] {max,index};
    }
}

## 풀이전략, 핵심 아이디어
# 반복문을 돌며 배열 안의 원소들을 max와 차례대로 비교
