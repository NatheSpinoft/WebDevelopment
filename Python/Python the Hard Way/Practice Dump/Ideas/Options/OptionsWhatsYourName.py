def names_menu():
    first_name = ""
    last_name = ""

    while True:
        print ("1. First name")
        print ("2. Last name")
        print ("3. Full name")
        print ("4. Quit")

        user_input = raw_input("Choose 1 - 4 : ")

        
        if user_input in ["1", "2", "3", "4"]:
            if user_input == "1":
                first_name = raw_input("What's the first name: ")
            elif user_input == "2":
                last_name = raw_input("What's the last name: ")
            elif user_input == "3":
                if first_name and last_name:
                    print "Your name is %s %s " % (first_name, last_name)
            elif user_input == "4":
                print ("Goodbye!")
                break
            else:
                print ("There is nothing more you can do")

names_menu()