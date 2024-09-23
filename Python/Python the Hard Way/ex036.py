from sys import exit

def red_portal():
    print("You see three buttons, yellow, green, and brown")
    btn_green = False
    btn_yellow = False
    btn_brown = False
    btn_enter = False

    print("Which buttons do you press?")
    btn_choice = input("> ").strip().lower().split()

    # Update button states based on input
    for choice in btn_choice:
        if choice in buttons:
            buttons[choice] = True

    btn_enter = input("Satisfied? (Y,N): ").strip().lower()

    if btn_enter == "y":
        print("Green: {}, Yellow: {}, Brown: {}".format(buttons['green'], buttons['yellow'], buttons['brown']))
    elif btn_enter == "n":
        print("I can't get no satisfaction!")
    else:
        print("Not a good selection...")

    print("You see, you conquered, and it smells real bad...")
    exit(0)

    #btn_choice = raw_input("> ").strip().lower()
    #if btn_choice == "green":
    #    btn_green = True
    #if btn_choice == "yellow":
    #    btn_yellow = True
    #if btn_choice == "brown":
    #    btn_yellow = True
    #    print("Interesting...")
    #    print("Choice: " + btn_choice)
    #btn_enter = raw_input("Satisfied? (Y,N): ").lower()
    #if btn_enter == "y":
    #    print(btn_green)
    #    print(btn_yellow)
    #    print(btn_brown)
    #    print(btn_choice)
    #elif btn_enter == "n":
    #    print("I can't get no satisfaction!")
    #else:
    #    print("Not a good selection...")

    print("You see, you conquered, and it smells real bad...")
    exit(0)

def fight(A):
    print("You pick up %s and fight") % A
 
def blue_portal():
    while True:
        print("You are in a marsh and see a boggish creature")
        print("You can run or you can fight")
        blue_choice = raw_input("> ").lower()
        if blue_choice == "run":
            print("You run but, it catches you and you died")
            exit(0)
        elif blue_choice == "fight":
            print("You see a sword, spear, and a dagger what do you pick up?")
            weapon = raw_input("> ").lower()
            if weapon == "sword" or weapon == "spear" or weapon == "dagger":
                print("You attack with %s, and survive") % weapon
                exit(0)
            else:
                print("Attacking with %s fails") % weapon
                exit(0)
def start():
    print ("You are alone in a room and two portals appear, one red and one blue")
    print ("Which portal do you jump?")
    jump_1 = raw_input("> ").lower()
    if jump_1 == "blue":
        blue_portal()
    elif jump_1 == "red":
        red_portal()
    else:
        print("You starve to die")

start()
