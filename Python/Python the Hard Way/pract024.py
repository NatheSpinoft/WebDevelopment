def mathing(start_point):
    a = start_point * 100
    b = a + 400
    c = b / 200
    return a, b, c

#the items below that are a b c are holders for the return items on a b c
the_input = int(raw_input("enter a number> "))
a, b, c = mathing(the_input)

selector = raw_input("select which letter from a, b, c > " )

if selector in ["a", "b", "c"]:
    if selector == "a":
        print a
    elif selector == "b":
        print b
    elif selector == "c":
        print c
    else:
        print selector 

print "the number from a = %d, b = %d, c = %d" % mathing(the_input)