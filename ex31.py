print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = input("> ")

if door == "1":
    print("There's a giant bear here easting a sheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your leg off. Good job!")
    else:
        print("Well, doing {bear} is probably better.")
        print("Bears runs away.")

elif door == "2":
        print("""You stare into the endless abyss at Cthulhu's retina.
        1. Blueberries.
        2. Yellow jacket clothespins.
        3. Understanding revolvers yelling melodies.""")

        insanity = input("> ")

        if insanity == "1" or insanity == "2":
            print("""Your body survives powered by a mind of jello.
Good job!""")
        else:
            print("""The insanity rots your eyes into a pool of muck.
Good job!""")

else:
    print("You stumble around and fall on a knife and die. Good job!")
