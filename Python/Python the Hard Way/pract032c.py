text = []

while True:
    emp_id = raw_input("Enter user id, [exit to leave]: ")
    if emp_id.lower() == "exit":
        print ("Exiting...")
        break
    name_id = raw_input("Enter a name: ")
    text.append({"ID":emp_id, "First name": name_id})

print ("\nEmployees:")
for msg in text:
    print ("ID: " + msg["ID"] + ", First name "+ msg["First name"])