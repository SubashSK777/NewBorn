public class Bidhsjdh {
  public static void main(String[] args) {
    Counter(10);
  }
  static void Counter (int n) {
    int i = 0;
    if (i == n) {
      return;
    } else {
      System.out.println(i);
      Counter(i + 1);
    }
  }
}
