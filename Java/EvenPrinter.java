import java.util.Scanner;

public class EvenPrinter {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter a Number: ");
    int n = sc.nextInt();
  }
  public static int Eventer (int n) {
    int i = 0;
    while (i < n) {
      System.out.println(i);
      i = i + 2;
    }
  }
}
