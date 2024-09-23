from sys import exit


def gunner():
    print("The gunner asks your name")
    name = raw_input("> ")
    print("Where would you like the bullet, %s?") % name
    die = raw_input("> ")
    if die == "head":
        dead("You died!")
    elif die =="stomach":
        print("Still alive")
        relive()
    else:
        dead("You get shot multiple times...")

def dead(why):
    print( "%s... It was an okay life") % why

def relive():
    while True:
        response = raw_input("Taunt? (Y/N)").lower()
        if response == "y":
            taunt = True
        elif response == "n":
            taunt = False
        else:
            dead("You survive for hours... death slowly waits")
        death = raw_input("Still want to die? (Y/N)").lower()
        if death == "y" and taunt == True:
            dead("Death!")
            exit(0)
        elif death == "y" and taunt == False:
            dead("Meh, pew!")
            exit(1)
        elif death == "n" and taunt == True:
            dead("hmmm.. pew pew")
            exit(2)
        else:
            dead("Shot through the heart and your too late!")
            exit(3)

gunner()
