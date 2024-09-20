# Initialize an empty list to store employee data
employees = []

# Loop to get employee data from user input
while True:
    # Ask the user for input
    emp_id = raw_input("Enter employee ID (or type 'exit' to finish): ")
    
    # Ensure emp_id is treated as a string and check if the user wants to exit the loop
    if str(emp_id).lower() == 'exit':
        break
    
    first_name = raw_input("Enter employee first name: ")
    
    # Add the employee data to the list
    employees.append({"ID": emp_id, "First Name": first_name})

# Print out the list of employees
print("\nEmployee List:")
for employee in employees:
    print("ID: " + employee["ID"] + ", First Name: " + employee["First Name"])
