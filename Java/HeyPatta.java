public class HeyPatta {

  public static void Square(int n) {
    for (int i = 1; i <= n; i++) {
      for (int j = 1; j <= n; j++) {
        System.out.print(j + " ");
      }System.out.println();
    }
  }

  public static void Triangle(int n) {
    for (int i = 0; i < n; i++){
      for (int j = 0; j <= i; j++){
        System.out.print(" * ");
      }System.out.println();
    }
  }

  public static void NumPat (int n) {
    for (int i = 0; i < n; i++){
      for (int j = 0; j < n; j++){
        if (j == 0 || j == n - 1 || i == 0 || i == n - 1 || i == j || i + j == n - 1 || i == n/2 || j == n/2) {
          System.out.print(" 1 ");
        } else {
          System.out.print("   ");
        }
      } System.out.println();
    }
  }

  public static void main(String[] args) {
    // Triangle(5);
    NumPat(100);
  }
}
