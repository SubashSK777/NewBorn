import java.util.*;
public class zxdfty {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int i = 0;
    int sum = 0;
    while (i < n){
      sum = sum + 2*i+1;
      i++;
    }
    System.out.println(sum);
  }
}
