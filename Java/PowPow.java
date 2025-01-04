import java.util.Scanner;

public class PowPow {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    int n = 4;
    int i = 0;
    int m = 2 ^ i;
    while (i < n) {
      System.out.println(m);
      i++;
    }
  }
}
