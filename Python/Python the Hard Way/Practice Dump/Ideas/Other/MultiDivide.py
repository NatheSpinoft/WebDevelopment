#! /usr/bin/python

individuals = 100

print("There are 100 individuals, 20 empty groups how many individuals per group can be set together.")
individuals_per_group = int(raw_input(">"))

group = individuals / individuals_per_group

if group == 5:
    print "The answer is ", False
else:
    print "The answer is ", True


