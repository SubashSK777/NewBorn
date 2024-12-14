public class LargestOfThree {
  public static void main(String[] args) {
    System.out.println(Greatest(27, 56, 0));
  }

  public static int Greatest (int x, int y, int z) {
    if (x > y && x > z) {
      return x;
    } else if ( y > x && y > z) {
      return y;
    } else {
      return z;
    }
  }
  
  
}