people = 30
cars = 40
buses = 40

if cars > people:
    print "We should take cars"
elif cars < people:
    print "We should not take cars"
else:
    print "We can't decide"

if buses > cars:
    print "That's too many buses"
elif buses < cars:
    print "Maybe we could take the bus"
else:
    print "We can't decide"

if people > buses:
    print "Alright, let's just take the buses"
else:
    print "Fine, lets stay home"
