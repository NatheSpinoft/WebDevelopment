print "You enter a dark room with two doors. Do you go through door #1 or #2"

door = raw_input()

if door == "1":
    print "There's a giant bear here eating cream cheese. What do you do?"
    print "1. Take the cake"
    print "2. Scream at the bear"

    bear = raw_input()

    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear == "2":
        print "The bear eats your legs off. Good job!"
    else:
        print "Well doing %s is probably better. Bear runs away" % bear

if door == "2":
    print "You stare into the abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespin"
    print "3. Understanding revolver yelling melodies"

    insanity = raw_input()

    if insanity == "1" or insanity =="2":
        print "Your body survived powered by a mind of jello. Good job"
    else:
        print "The insanity rots into your eyes into a pool of muck. Good job"

else:
    print "You stumble around and fall on a knife, lucky!"
    