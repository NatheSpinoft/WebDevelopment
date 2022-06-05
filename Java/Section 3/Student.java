class Student {    
    int id = 1000;	//literal expression
	
	void compute() {	    
		int nextId = id + 1; 
		
	    System.out.println("id: " + id);
		System.out.println("nextId: " + nextId);
	}
	
	public static void main(String[] args) { //runs this program
	    Student s = new Student();
		s.compute();
	}
}