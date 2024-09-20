models = []

while True:
    print ("1. Enter model")
    print ("2. view models")
    print ("3. print into txt")
    user_input = raw_input("Enter option [Q] to quit: ").lower()
    if user_input != "q":
        if user_input == "1":
            while True:
                mod_id = raw_input("Enter model [Q] to stop: ").lower()
                if mod_id == "q":
                    break
                make_id = raw_input("Enter make: ")
                models.append({"Model": mod_id, "Make": make_id})
        elif user_input == "2":
            for model in models:
                print("Model: " + model["Model"] + " Make: " + model["Make"])
        elif user_input == "3":
            if models:
                with open("Qmodels.txt", "w") as file:
                    for model in models:
                        file.write("Model: " + model["Model"] + " Make: " + model["Make"] + "\n")
                print("Successfully sent to Qmodels.txt")
            else:
                print ("Select a proper option")
    else:
        print ("Goodbye")
        break
