class Solution {
    public String solution(String[] cards1, String[] cards2, String[] goal) {
        int idx1 = 0;
        int idx2 = 0;
        
        for (String target : goal) {
            if (idx1 < cards1.length && cards1[idx1].equals(target)) {
                idx1++;
            } else if (idx2 < cards2.length && cards2[idx2].equals(target)) {
                idx2++;
            } else {
                return "No";
            }
        }
        return "Yes";
    }
}

// 풀이전략, 핵심 아이디어
// 각 카드 뭉치의 현재 위치를 가리킬 포인터 변수를 각각 두고
// goal을 순회하면서 알맞은 카드를 제거시켜나가는 방식
