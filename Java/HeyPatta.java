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

  public static void HollowSqr(int n) {
    for (int i = 1; i <= n; i++) {
      for (int j = 1; j <= n; j++) {
        if (i == 1 || j == n-1 || i == n-1 || j == 1) {
          System.out.print(" * ");
        }
        else {
          System.out.print("   ");
        }

      }
      System.out.println();
    }
  }

  public static void NumTriangle(int n) {
    int sum = 0;
    for (int i = 0; i < n; i++) {
      for ( int j = 0; j < i; j++) {
        sum = sum + 1;
        System.out.printf("%02d",sum);
        System.out.print(" ");
      }System.out.println();
    }
  }

  public static void Crossbreed (int n) {
    for (int i = 0; i <= n; i ++) {
      for (int j = 0; j <= i; j++) {
        if (j == 0 || j == i) {
          System.out.print(" * ");
        } else {
          System.out.print("   ");
        }
      } System.out.println();
    }  

    for (int i = 1; i <= n; i++) {
      for (int j = 1; j <= n ; j++) {
        if (j == 1 || i + j - 1 == n) {
          System.out.print(" * ");
        } else {
          System.out.print("   ");
        }

      } System.out.println();
    }
  }

  public static void main(String[] args) {
    // Triangle(5);
    // NumPat(11);
    // HollowSqr(11);
    // NumTriangle(5);
    Crossbreed(5);


  }
}
