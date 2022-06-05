class CurrencyConverter {
	int rupee = 63;
	int dirham = 3;
	int real = 3; 
	int chilean_peso = 585;
	int mexican_peso = 18;
	int _yen = 107;
	int $australian = 2;
	int dollar = 1;
		
		void printCurrencies () {
			System.out.println("rupee: " + rupee);
			System.out.println("$australian: " + $australian); 
		}
		
		public static void main(String[] args) {
		CurrencyConverter cc = new CurrencyConverter();
		cc.printCurrencies();
		}
}