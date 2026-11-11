import java.util.Scanner;
class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();

        String row = "*".repeat(a);
        
        for (int i=0; i<b; i++) {
            System.out.println(row);
        }
    }
}

// 풀이전략, 핵심 아이디어
// void 메서드이므로 System.out.println() 사용
// Scanner를 사용하여 사용자로부터 입력받게 하기
