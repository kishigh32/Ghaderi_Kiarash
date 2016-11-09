print("If you roll higher than the computer, winner is you.\nIf computer rolls higher, winner is computer.")


def rollDice():
    import random
    player = random.randint(1, 6)
    computer = random.randint(1,6)

    print("You rolled a" ,player)
    print("Computer rolled a" ,computer)

    if player > computer:
        print("The winner is you!")

    if computer > player:
        print("The winner is computer!")

    if player == computer:
        print("You and computer tied!")

rollDice()
