import java.util.ArrayList;
import java.util.Scanner;

public class bridv {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    ArrayList<Integer> arr = new ArrayList<>();

    while(true) {
      int n = sc.nextInt();

      if (n != -1) {
        arr.add(n);
      } else {
        System.out.println();
        break;
      }
    }
  }
}