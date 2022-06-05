class Student {
	// Variable Desclarations
	int id;
	String name;
	String gender;
	
	//method definitions
	boolean updateProfile{String newName) {
		name = newName;
		return true;
	}
}

class StudentTest {
	public static void main (String args) {
		//1. creating a new student object
		Student s = new Student();
		
		//2. setting Student's state
		s.id = 1000;
		s.name = "joan";
		s.gender = "male";
		
		//3.updating profile with correct name
		s.updateProfile("john");
	}
}