class Solution {
    public int solution(int[][] sizes) {
        int maxwidth = 0;
        int maxheight = 0;
        
        for (int[] card : sizes) {
            int width = Math.max(card[0],card[1]);
            int height = Math.min(card[0],card[1]);
            
            maxwidth = Math.max(maxwidth,width);
            maxheight = Math.max(maxheight,height);
        }
        return maxwidth * maxheight;
    }
}

// 풀이전략, 핵심 아이디어
// 긴 변은 긴 변끼리, 짧은 변은 짧은 변끼리 모으는 것이 지갑 크기를 줄이는 핵심
