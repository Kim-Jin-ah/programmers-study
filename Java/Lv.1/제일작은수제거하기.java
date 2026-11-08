class Solution {
    public int[] solution(int[] arr) {
        if (arr.length == 1) {return new int[]{-1};}
        
        int min = arr[0];
        for (int i=1; i<arr.length; i++) {
            if (arr[i] < min) {
                min = arr[i];
            }
        }
        
        int[] answer = new int[arr.length -1];
        int index = 0;
        for (int i=0; i<arr.length; i++) {
            if (arr[i] != min) {
                answer[index] = arr[i];
                index++;
            }
        }
        return answer;
    }
}

// 풀이전략, 핵심 아이디어
// 배열의 길이가 1인지 확인 후 가장 작은 값을 찾아, 그 수를 제외한 배열 만들기
// Stream을 사용한다면
class Solution {
    public int[] solution(int[] arr) {
        if (arr.length == 1) {
            return new int[]{-1};
        }
      
        int min = Arrays.stream(arr).min().getAsInt();
        return Arrays.stream(arr)
                     .filter(n -> n != min)
                     .toArray();
    }
}
