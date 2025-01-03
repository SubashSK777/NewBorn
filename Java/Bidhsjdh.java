public class Bidhsjdh {
  public static void main(String[] args) {
    Facto(5);
  }

  static int Facto(int n) {
    int res = 1;
    for ( int i = 1; i <= n; i++) {
      res *= res*i;
      return res;
    }
  }
}
