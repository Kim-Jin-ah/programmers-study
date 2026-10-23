class Solution {
    public int solution(int slice, int n) {
        if ((n % slice)!=0) {
            return n / slice + 1;
        } else {return n/slice;}
    }
}

## 풀이전략, 핵심 아이디어
# if문으로 나머지를 이용해 필요한 판 수 구하기

# if문을 사용하지 않고 한 줄로 쓰는 방식
class Solution {
    public int solution(int slice, int n) {
        return (n + slice - 1) / slice;
    }
}
