import java.util.Scanner;

public class PowPow {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    int n = sc.nextInt();
    while (n % 2 == 0){
        n = n / 2;  
    }
    if (n == 1) {
      System.out.println("Is a Power");
    } else {
      System.out.println("Not a Power");
    }
  }
}
