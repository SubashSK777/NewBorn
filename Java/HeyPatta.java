public class HeyPatta {
  public static void Square(int n) {
    for (int i = n; i < n; i++) {
      for (int j = n; j < n; j++) {
        System.out.print("*");
      }
    }
  }

  public static void main(String[] args) {
    Square(5);
  }
}
