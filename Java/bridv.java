import java.util.*;

public class Main {
  public static void main (String[] args) {
    Scanner sc = new Scanner(System.in);
    long n = sc.nextLong();
    long a = 0;
    long b = 1;
    System.out.print(b+" ");
    for (int i = 1; i < n; i++){
      long next = a + b;
      a = b;
      b = next;
      System.out.print(next +" ");
    } 
  }
}