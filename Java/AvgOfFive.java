public class AvgOfFive {
  public static void main(String[] args) {
    System.out.println(BigOrSmall(0, 0, 0, 0, 0));
  }
  public static String BigOrSmall (int a, int b, int c, int d, int e) {
    int Avg = (a + b + c + d + e) / 5;
    if (Avg > 50) {
      return "It is Greater Than 50";
    } else {
      return "It is Smaller Than 50";
    }

  }
}
