#!/usr/bin/env python3 

print("""You enter a dark room with two doors. 
Do you go through door #1 or door #2 or door #3""")


door = input("-> ")

# == Door Number 1 logic =======================
if door == "1":

    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?\n")

    print("1. Take the cake.")
    print("2. Scream at the bear.")

    # == Bear logic ============================
    bear = input("-> ")

    if bear == "1":
        print("1) The bear eats your face off. Good job!")
    elif bear == "2":
        print("2) The bear eats your legs off. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

# == Door Number 2 Logic =====================
elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.\n")
    
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")
    
 # == Insanity Logic ======================
    insanity = input("-> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")
# == Door Number 3 Logic =====================
elif door == "3":
    print("You see yourself staring at 3 doors.\n")
    
    print("1. hit yourself over the head")
    print("2. tell yourself to choose no doors because that band sucks")
    print("3. close the door and turn around")
    
 # == Paradox Logic ======================
    paradox = input("-> ")

    if paradox == "1" or paradox == "2":
        print(" A star trek like cascade of paradoxes destroys the universe")
        print(" can nothingness be empty?")
    else:
        print("you find yourself at a computer coding python")
        print("Good job!")
else:
    print("You did not select a door??? Good Call :)")
