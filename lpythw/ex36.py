def lust_room():
    print("It a pink room, a little bit dark but dim light.")
    print(
        "The smell in the room capture you, it's not the best you've ever smell, but you definitely recall."
    )
    print(
        "Here's something around you, really beautiful, pretty, you could not even tell what it is, all you want to do is have sex!!!"
    )
    print("something poped up in you mind: ")
    choice = input("fuck or leave?\n> ")
    if 'fuck' == choice:
        print(
            "That was amazing, best sex you ever have, you want it again, but in this version1.0, you have to leave."
        )
        dead(
            "you feel like everything of you is taken, but with the greatness delight."
        )
    elif 'leave' == choice:
        print(
            "You choose to leave, but suddenly you have a sight that what other peoples do, and it harmless to just have this nice thing, you feel a little regret but you have to leave(1.0)."
        )
    else:
        print("can't understand you, must choose one of them.")
        lust_room()
    print(
        "no matter what you experienced, the room gone, and you can't came back(1.0)."
    )
    gluttony_room()


def gluttony_room():
    print("Bunch of food, just wan to eat them forever.")
    print("Before you eat, choose from: eat or leave.")
    input("> ")
    choice = input("eat or leave")
    if 'eat' == choice:
        print("What a delicious meal!")
        dead("each too much, more than you could, stomach explode. ")
    elif 'leave' == choice:
        print("What? leave? you are crazy")
        exit(0)


def greed_room():
    pass


def sloth_room():
    pass


def wrath_room():
    pass


def envy_room():
    pass


def pride_room():
    pass


def start(right_choice):
    print("The only meaning you here is make choice, so...")
    print("Here's choice, enter or death?")
    choice = input("enter or death\n> ")
    print(f"This is your {choice}")
    if 'enter' == choice:
        lust_room()
    elif 'death' == choice:
        dead("if that's what you want")
    else:
        if not right_choice:
            print("I will give you one more chance.")
            start(True)
        else:
            dead("I do offer you a choice")


def dead(why):
    # maybe could use a switch to different endings
    print(why)
    print(
        "Seems you are dead, no worry, lot of people do, and animails, even planet could die."
    )
    print(
        "Die means gone, nothing will exist for you, you could finally get rid of everything, maybe that is what eternity means"
    )
    exit(0)


start(False)
