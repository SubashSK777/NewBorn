public class Tabla {
  public static void main(String[] args) {
    int n = 4;
    for (int i = 1; i < n; i++) {
      i = i^i;
      if (i == n) {
        System.out.println("Perfect Square");
      } else {
        System.out.println("Not a Perfect Square");
      }
    }
  }
}