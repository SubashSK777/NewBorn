public class Javam {
	static void LoanChecker (int age, int salary) {
		if (age < 18) {
			if (salary < 25,000) {
				System.out.println("Eligible for Loan");
			}	
		} System.out.println("Not Eligible");

	public static void main (String [] args) {
		LoanChecker(20, 15,000);
	}
}