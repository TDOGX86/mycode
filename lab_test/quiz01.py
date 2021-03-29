#!/usr/bin/env python3


name = input ("What is your Name?")
day = input("What day of the week is it?")

# printing objects
        print("Hello, ",name,"!"," Happy ",day,"!",sep="")
        # concatenation using + signs
        print("Hello, " + name + "! Happy " + day + "!")
        # .format
        print("Hello, {}! Happy {}!".format(name, day))
        # f string
        print(f"Hello, {name}! Happy {day}!")
