class Solution {
    public double solution(int[] arr) {
        double sum = 0;
        for (int num : arr) {
            sum += num;
        }
        return sum / arr.length;
    }
}

// 향상된 for문으로 sum을 구하고 전체 개수로 나누기
