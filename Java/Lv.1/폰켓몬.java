import java.util.HashSet;
class Solution {
    public int solution(int[] nums) {
        HashSet<Integer> set = new HashSet<>();
        for (int num : nums) {
            set.add(num);
        }
        
        int target = nums.length / 2;
        
        return Math.min(set.size(),target)
    }
}

// 풀이전략, 핵심 아이디어
// 중복을 제거한 폰켓몬의 종류 개수 구하기 위해 HashSet 사용
// 폰켓몬 종류의 총 개수와 가질 수 있는 최대 수 중 더 작은 값을 리턴
