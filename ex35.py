# 习题 35: 分支和函数

from sys import exit  # 推荐在脚本开头加上这行导入[2](@ref)


def dead(why):
    print(why, "Good job!")

    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take? (left or right)")

    next = input("> ").lower()  # 获取输入并转换为小写

    if next == "left":
        # 假设向左走进入熊的房间
        bear_room()
    elif next == "right":
        # 假设向右走进入克苏鲁的房间
        cthulhu_room()
    else:
        # 如果输入既不是"left"也不是"right"，游戏结束
        dead("You stumble around until you starve.")
def gold_room():
    print("This room is full of gold.How much do you take ?")

    next =input(">")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy,you win!")
        exit(0)
    else:
        dead("You greedy bastard!")

def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door!")
    print("How are you going to move the bear?")
    bear_move = False

    while True:
        next = input(">")

        if next == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif next == "taunt bear" and not bear_move:
            print("The bear gets pissed off and chews your leg off.")
            bear_move = True
        elif next == "open door" and bear_move:
            gold_room()

        else:
            print("I get no idea what that means.")

def cthulhu_room():
    print("Here you see the great evil Cthulhu.")

    print("He, it, whatever stares at you and you go insane.")

    print("Do you flee for your life or eat your head?")

    next = input(">")
    if "flee" in next:
        start()

    elif "head" in next:
        dead("Well that was tasty.")

    else:
        cthulhu_room()


start()


