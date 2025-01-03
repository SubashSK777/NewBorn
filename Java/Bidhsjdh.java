public class Bidhsjdh {
  public static void main(String[] args) {
    Counter(10);
  }
  static void Counter (int n) {
    if (n == 0) {
      return;
    } else {
      System.out.println(n);
      Counter(n - 1);
    }
  }
}
