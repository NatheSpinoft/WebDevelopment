from sys import exit
import time

def red_portal():
    while True:

        print("You see three buttons, yellow, green, and brown")
        btn_green = False
        btn_yellow = False
        btn_brown = False

        print("Which buttons do you press?")
        btn_choice = input("> ").strip().lower()

        if "yellow" in btn_choice:
            btn_yellow = True
            print("You hear flies and a *clunk*")
            time.sleep(1)
        if "brown" in btn_choice:
            btn_brown = True
            print("You hear *Clunk*")
            time.sleep(1)
        if "green" in btn_choice:
            btn_green = True
            print("You smell a faint scent of grass")
            time.sleep(1)

        print("There is a stone that has a reset and confirm button which do you choose?")
        choice_A = input("> ").lower()
        if choice_A == "confirm":
            if btn_brown == True and btn_green == True:
                print("YOU WIN!")
                exit(1)
            else:
                print("The game restarts")
                start()


def fight(A):
    print("You pick up %s and fight") % A
 
def blue_portal():
    while True:
        print("You are in a marsh and see a boggish creature")
        print("You can run or you can fight")
        blue_choice = input("> ").lower()
        if blue_choice == "run":
            print("You run but, it catches you and you died")
            exit(0)
        elif blue_choice == "fight":
            print("You see a sword, spear, and a dagger what do you pick up?")
            weapon = input("> ").lower()
            if weapon == "sword" or weapon == "spear" or weapon == "dagger":
                print("You attack with %s, and survive") % weapon
                exit(0)
            else:
                print("Attacking with %s fails") % weapon
                exit(0)
def start():
    print ("You are alone in a room and two portals appear, one red and one blue")
    print ("Which portal do you jump?")
    jump_1 = input("> ").lower()
    if jump_1 == "blue":
        blue_portal()
    elif jump_1 == "red":
        red_portal()
    else:
        print("You starve to die")

start()