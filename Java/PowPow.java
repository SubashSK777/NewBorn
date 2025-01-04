import java.util.Scanner;

public class PowPow {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    int n = sc.nextInt();
    int i = 0;
    while (i % 2 == 0){
        n = n / 2;
        
    }
    if (n == 1) {
      System.out.println("Not a Power");
    } else {
      System.out.println("Is a Power");
    }
  }
}
