# 习题 31: 作出决定
print("you enter a drak room with two doors . Do you go through door #1 or door #2?")

door = input(">")

if door == "1":
    print("There's giant bear here eating a cheese cake. What do you do ?")
    print("1.Take the cake.")
    print("2.Scream at the bear.")

    bear = input(">")

    if bear == "1":
        print("There bear eats your face off. Good job!")


    elif bear == "1":
        print("The bear eats your legs off . Good job!")

    else:
        print(f"Well , doing {bear}  is probably better .Bear runs away.")

elif door =="2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1.Buleberries.")
    print("2.Yellow jacket clothespains")
    print("3.Understanding revolvers yelling melodies.")

    insanity = input(">")

    if insanity == "1" or insanity == "2":
        print("Your boby survives powered by a mind of jello . Good job!")

    else:
        print("The insanity rots your eyes into a pool of muck . Good job !")
        print("You stumble around and fall on a knife and die. Good job!")
