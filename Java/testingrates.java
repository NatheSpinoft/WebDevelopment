class Rates {
	int GST = 130;
	int couch = 1000;
	
	void computeRates() {
		int total = GST + couch;
	
		System.out.println("GST is: " + GST);
		System.out.println("item is: " + couch);
		System.out.println("total is: " + total);
	}
	public static void main(String[] args) {
		Rates rr = new Rates();
		rr.computeRates();
	}
}