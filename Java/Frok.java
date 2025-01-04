import java.util.*;

public class Frok {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int sum = 0;
    int j = 0;
    for (int i = 0; i < n; i++) {
      j = 2*i+1;
      sum = sum + 2*i+1;
    }
  }
}
