import java.util.Scanner;

public class EvenPrinter {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter a Number: ");
    int n = sc.nextInt();
    System.out.println(Eventer(n));
  }
  public static int Eventer (int n) {
    int i = 0;
    while (i < n) {
      return i;
      i = i + 2;
    }
  }
}
