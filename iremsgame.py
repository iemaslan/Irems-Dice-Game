welcome = " \033[45m \033[97m LADIES AND GENTLEMEN, WELCOME TO IREM'S GAMEEEEE :) <3  \033[0m"
print(welcome)
name1 = input("\033[1m\033[35mPlayer 1, please enter your name to get started:")
name2 = input("\033[97mPlayer 2, please enter your name to get started:")


squares = [
    {
        "penalty": -1,
        "reward": -1
    },
    {
        "penalty": -1,
        "reward": -1
    }
]
squares[0]["penalty"] = int(input("\033[1m\033[35m------> %s, Choose the number of penalty from 1 to 100: " % (name1)))
squares[0]["reward"] = int(input("------> %s, Choose the reward number between 1 and 100: " % (name1)))
squares[1]["penalty"] = int(input("\033[97m------> %s, Choose the number of penalty from 1 to 100: " % (name2)))
squares[1]["reward"] = int(input("------> %s, Choose the reward number between 1 and 100: " % (name2)))
location = [0 , 0]



while location[0] <= 100 and location[1] <= 100:

    start = str(input("\033[1m\033[35m %s, Press enter to roll the dice" % (name1)))
    print("Rolling the Dice...")



    import random
    def visualize_dice(dice1):
        dicee1 = """    -----------------
    |                |
    |                |
    |       0        |
    |                |
    |                |
    ------------------"""

        dicee2 = """    ------------------
    |                |
    |  0             |
    |                |
    |            0   |
    |                |
    ------------------"""

        dice3 = """    ------------------
    | 0              |
    |                |
    |       0        |
    |                |
    |             0  |
    ------------------"""

        dice4 = """    ------------------
    |  0          0  |
    |                |
    |                |
    |                |
    |  0          0  |
    ------------------"""

        dice5 = """    ------------------
    |  0          0  |
    |                |
    |       0        |
    |                |
    |  0          0  |
    ------------------"""

        dice6 = """    ------------------
    | 0            0 |
    |                |
    | 0            0 |
    |                |
    | 0            0 |
    ------------------"""

        if dice1 == 1:
            print(dicee1)
        elif dice1 == 2:
            print(dicee2)
        elif dice1 == 3:
            print(dice3)
        elif dice1 == 4:
            print(dice4)
        elif dice1 == 5:
            print(dice5)
        else:
            print(dice6)

    dice1 = random.randint(1, 6)
    print('dice number:' + str(dice1))
    visualize_dice(dice1)
    location[0] = location[0] + dice1

    print(f" %s rolled {dice1} on the dice" % (name1))

    if location[0] == squares[0]["penalty"] or location[0] == squares[1]["penalty"]:
        location[0] = location[0] - 10
        print(f" \033[91m UPPPS :( %s in the penalty frame, go BACK<-- 10 squares. " % (name1))

    if location[0] == squares[0]["reward"] or location[0] == squares[1]["reward"]:
        location[0] = location[0] + 10
        print(f" \033[92m YEEEEEEYYY :) %s in the reward square, go FORWARD--> 10 squares. " % (name1))

    if location[0] < 100:
        print(f" %s is now {location[0]}th square. \n" % (name1))


    else:
        print(" \033[92m %s WON :)" % (name1))
        print(" \033[92m WINNER WINNER CHICKEN DINNERRRRRR")
        break



    start2 = str(input(" \033[97m %s, Press enter to roll the dice" % (name2)))
    print("Rolling the Dice...")

    import random
    def visualize_dice(dice2):
        dicee1 = """    -----------------
    |                |
    |                |
    |       0        |
    |                |
    |                |
    ------------------"""

        dicee2 = """    ------------------
    |                |
    |  0             |
    |                |
    |            0   |
    |                |
    ------------------"""

        dice3 = """    ------------------
    | 0              |
    |                |
    |       0        |
    |                |
    |             0  |
    ------------------"""

        dice4 = """    ------------------
    |  0          0  |
    |                |
    |                |
    |                |
    |  0          0  |
    ------------------"""

        dice5 = """    ------------------
    |  0          0  |
    |                |
    |       0        |
    |                |
    |  0          0  |
    ------------------"""

        dice6 = """    ------------------
    | 0            0 |
    |                |
    | 0            0 |
    |                |
    | 0            0 |
    ------------------"""

        if dice2 == 1:
            print(dicee1)
        elif dice2 == 2:
            print(dicee2)
        elif dice2 == 3:
            print(dice3)
        elif dice2 == 4:
            print(dice4)
        elif dice2 == 5:
            print(dice5)
        else:
            print(dice6)



    dice2 = random.randint(1, 6)
    print('dice number:' + str(dice2))
    visualize_dice(dice2)
    location[1] = location[1] + dice2

    print(f" %s rolled {dice2} on the dice" % (name2))

    if location[1] == squares[0]["penalty"] or location[1] == squares[1]["penalty"]:
        location[1] = location[1] - 10
        print(f" \033[91m UPPPPPSSSS :( %s in the penalty frame, go BACK<-- 10 squares." % (name2))

    if location[1] == squares[0]["reward"] or location[1] == squares[1]["reward"]:
        location[1] = location[1] + 10
        print(f" \033[92m YEEEEEYYY :) %s is in the reward frame, go FORWARD--> 10 squares." % (name2))

    if location[1] < 100:
        print(f" %s is now {location[1]}th square. \n" % (name2))

    else:
        print(" \033[92m %s WON :)" % (name2))
        print(" \033[92m WINNER WINNER CHICKEN DINNEEERRRR")
        break






















