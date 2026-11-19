class Solution {
    public String solution(int a, int b) {
        String[] days = {"FRI","SAT","SUN","MON","TUE","WED","THU"};
        int[] monthdays = {31,29,31,30,31,30,31,31,30,31,30,31};
        int total = b - 1;
        
        for (int i=0; i<a-1; i++) {
            total += monthdays[i];
        }
        
        return days[total % 7];
    }
}

// 풀이전략, 핵심 아이디어
// 해당 달 전까지 수를 더하고, 날짜를 더한 후
// 요일을 나눗셈의 나머지 원리를 이용해 리턴
