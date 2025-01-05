public class HeyPatta {

  public static void Square(int n) {
    for (int i = 1; i <= n; i++) {
      for (int j = 1; j <= n; j++) {
        System.out.print("*");
      }System.out.println();
    }
  }

  public static void main(String[] args) {
    Square(5);
    
  }
}
