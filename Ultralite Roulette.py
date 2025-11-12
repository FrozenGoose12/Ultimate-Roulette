import random
import time
print("Welcome to Ultimate Roulette Ultra Lite!")
def wheel():
    print("Red numbers:\n1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36\n")
    print("Black numbers:\n2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35\n")
    print("Green numbers:\n0, 00\n")
wheel()
chips = 500
while True:
    if chips == 0:
        print("You have been wiped out. Better luck next time!")
        break
    while True:
        color = input("Make your selection (Red or Black): ")
        color = color.replace(" ", "").replace(".", "").replace("!", "").upper()

        if color == "RED" or color == "BLACK":
            print(f"You have chosen {color}!")
            break
        else:
            print("\nPlease choose Red or Black")
    while True:
        try:
            print()
            bet = int(input(f"Place your bet in chips (You have {chips} chips): "))

            if bet <= 0:
                print("Please place a bet greater than 0 chips.")
            elif bet > chips:
                print("You do not have enough chips to place that bet. Please try again.")

            else:
                break

        except ValueError:
            print("Please enter a whole number amount of chips")
    print(f"You have placed your bet of {bet} chips!\n")
    print("Spinning Wheel and Ball...\n")
    time.sleep(2)
    slot = random.randint(0, 37)
    if slot == 37: #GREEN
        print(f"The ball landed on slot 00")
        print("GREEN!")
        c = "green"
    else:
        print(f"The ball landed on pocket {slot}", end = " — ")
        if slot in [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]: #RED
            print("RED!")
            c = "RED"
        elif slot in [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]: #BLACK
            print("BLACK!")
            c = "BLACK"
        elif slot == 0: #GREEN
            print("GREEN!")
            c = "GREEN"
    time.sleep(1)

    if c == color:
        print(f"Your selection of {color.lower()} was a Hit!\n")
        print(f"You won {bet} chips!")
        chips += bet
        print(f"You now have {chips} chips (${chips * 100}).")
    else:
        print(f"The ball did not land on {color.lower()}.\n")
        chips -= bet
        print(f"You now have {chips} chips (${chips * 100}).")
