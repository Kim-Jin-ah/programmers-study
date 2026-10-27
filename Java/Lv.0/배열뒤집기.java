class Solution {
    public int[] solution(int[] num_list) {
        int[] answer = new int[num_list.length];
        
        for (int i=0; i<num_list.length; i++) {
            answer[i] = num_list[num_list.length-1-i];
        }
        return answer;
    }
}

## 풀이전략, 핵심 아이디어
# 리턴할 배열의 크기를 넣어 새로운 빈 배열을 생성한 후
# 반복문을 돌며 기존 배열의 뒤쪽 원소를 새 배열의 앞쪽부터 저장하기
