#!/usr/bin/python3
import sys 

def counterpush():
    count = 0 

    while True:
        print("Say magic")
        text = raw_input("> ")
        words = text.split()
        for word in words:
            if word == "magic":
                count += 1
            elif word == "q":
                exit(0)
            else:
                pass
        print("count: %d " % count)

counterpush()