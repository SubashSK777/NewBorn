public class Bidhsjdh {
  public static void main(String[] args) {
    Counter(10, 0);
  }
  static void Counter (int n, int i) {
    if (i == n) {
      return;
    } else {
      System.out.println(i);
      Counter(n, i + 1);
    }
  }
}
