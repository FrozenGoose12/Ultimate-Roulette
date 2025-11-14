import random
import time
#default settings
n = 100 #chip multiplier
s = 2 #wheel delay
t = 1 #reveal delay
wipeout = 0

def wheel():
    print("\nRed numbers:\n1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36\n")
    print("Black numbers:\n2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35\n")
    print("Green numbers:\n0, 00\n")

def token(chips, n):
    print(f"You now have {chips} chips (${chips * n}).\n")

print("Welcome to Ultimate Roulette!\n")

while True:
    print("Start Menu: ")
    print("1. Help\n2. Settings\n")

    while True:
        start = input("Press Enter to begin: ")
        if start == "1" or start == "2" or start == "":
            break
        else:
            print("Please select 1, 2, or hit Enter to start\n")

    if start == "":
        break
    elif start == "1":
        print("Classic Bets:\n1. Red/Black (Payout 1:1)\n2. Odd/Even (Payout 1:1)\n3. High/Low (Payout 1:1)\n4. Dozen (Payout 2:1)\n\nHigh Risk High Reward:\n5. Straight Up (Payout 35:1)\n6. Split (Payout 17:1)\n7. Street (Payout 11:1)\n8. Corner (Payout 8:1)\n9. Basket (Payout 6:1)\n10. Double Street (Payout 5:1)\n\nMisc:\n11. Show Wheel\n12. Back\n")
        while True:
            try:
                help = int(input("Select the bet type that you need help with: "))
                if 0 < help < 13:
                    break
                else:
                    print("Please choose an option 1-12\n")
            except ValueError:
                print("Please choose an option 1-12\n")

        if help == 1:
            print("Bet red or black. If the ball lands on the color you selected, you win!")
        elif help == 2:
            print("Bet odd or even. If the ball lands on the parity you selected, you win!")
        elif help == 3:
            print("Bet high (19-36) or low (1-18). If the ball lands on the magnitude you selected, you win!")
        elif help == 4:
            print("Bet on one of three dozens (1-12), (13-24), or (25-36). If the ball lands on the dozen you selected, you win!")
        elif help == 5:
            print("Bet on one number (00, 0-36). If the ball lands on the number you selected, you win big!")
        elif help == 6:
            print("Bet on two adjacent numbers (on the flat roulette table). If the ball lands on one of the two numbers you selected, you win!")
        elif help == 7:
            print("Bet on one row (on the flat roulette table). If the ball lands on the street/row you selected, you win!")
        elif help == 8:
            print("Bet on the lowest number of a corner to form a square (on the flat roulette table).\nIf the ball lands on one of the four numbers/corners that make up the square you selected, you win!")
        elif help == 9:
            print("This choice automatically bets on 0, 00, 1, 2, and 3 which forms a basket on the flat roulette table.\nIf the ball lands on any of those numbers, you win!")
        elif help == 10:
            print("Bet on a two adjacent rows (on the flat roulette table).\nIf the ball lands on any of the six numbers within the double street you selected, you win! ")
        elif help == 11:
            wheel()
        print()
        if help == 12:
            continue
            
    elif start == "2":
        print("\n1. Set Chip Value\n2. Set Wheel Delay\n3. Set Reveal Delay\n4. Back\n")
        while True:
            try:
                settings = int(input("Select Setting: "))
                if settings in [1, 2, 3, 4]:
                    print()
                    break
                else:
                    print("Please select setting option 1-4\n")
            except ValueError:
                print("Please select setting option 1-4\n")

        while True:
            if settings == 1:
                try:
                    n = int(input("Enter chip value: "))
                    if n <= 0:
                        print("Please select a positive whole number greater than 0\n")
                    else:
                        print()
                        break
                except ValueError:
                    print("Please select a positive whole number greater than 0\n")

            elif settings == 2:
                try:
                    s = int(input("Enter wheel delay (seconds): "))
                    if s < 0:
                        print("Please select a positive whole number\n")
                    else:
                        print()
                        break
                except ValueError:
                    print("Please select a positive whole number\n")

            elif settings == 1:
                try:
                    t = int(input("Enter reveal delay (seconds): "))
                    if t < 0:
                        print("Please select a positive whole number\n")
                    else:
                        print()
                        break
                except ValueError:
                    print("Please select a positive whole number\n")

            elif settings == 4:
                break
while True:
    while True:
        try:
            chips = int(input(f"Enter Starting Amount of Chips (1 chip = ${n}): "))
            if chips <= 0:
                chips = int(input("Please enter a value above 0: "))
            else:
                if chips == 1:
                    print(f"You have 1 chip (equivalent to ${n})")
                else:
                    print(f"You have {chips} chips (equivalent to ${chips * n})\n")
                break

        except ValueError:
            print("Please enter a whole number")
            print()


    while True:
        if chips == 0:
            print("You have been wiped out. Better luck next time!")
            wipeout += 1
            print(f"Wipeout #{wipeout}\n")
            break

        while True:
            print("Classic Bets:\n1. Red/Black (Payout 1:1)\n2. Odd/Even (Payout 1:1)\n3. High/Low (Payout 1:1)\n4. Dozen (Payout 2:1)\n\nHigh Risk High Reward:\n5. Straight Up (Payout 35:1)\n6. Split (Payout 17:1)\n7. Street (Payout 11:1)\n8. Corner (Payout 8:1)\n9. Basket (Payout 6:1)\n10. Double Street (Payout 5:1)\n")
            try:
                btype = int(input("Choose your bet type: "))
                if 0 < btype < 11:
                    break
                else:
                    print("Please choose an option 1-10\n")
            except ValueError:
                print("Please choose an option 1-10\n")

        print()
        if btype == 1:
            print("You have chosen Red/Black!")
            while True:
                color = input("Make your selection (Red or Black): ")
                color = color.replace(" ", "").replace(".", "").replace("!", "").upper()

                if color == "RED" or color == "BLACK":
                    print(f"You have chosen {color}!")
                    break
                else:
                    print("\nPlease choose Red or Black")


        elif btype == 2:
            print("You have chosen Odd/Even!")
            while True:
                parity = input("Make your selection (Odd or Even): ")
                parity = parity.replace(" ", "").replace(".", "").replace("!", "").upper()

                if parity == "ODD" or parity == "EVEN":
                    print(f"You have chosen {parity}!")
                    break
                else:
                    print("\nPlease choose Odd or Even")


        elif btype == 3:
            print("You have chosen High/Low! (Low = 1-18, High = 19-36)")
            while True:
                magnitude = input("Make your selection (High or Low): ")
                magnitude = magnitude.replace(" ", "").replace(".", "").replace("!", "").upper()

                if magnitude == "HIGH" or magnitude == "LOW":
                    print(f"You have chosen {magnitude}!")
                    break
                else:
                    print("\nPlease choose High or Low")

        elif btype == 4:
            print("You have chosen Dozen!")
            print("Dozen Types:\n1. 1-12\n2. 13-24\n3. 25-36")

            while True:
                egg = input("Make your selection: ")

                if egg not in ["1", "2", "3"]:
                    print("Please choose an option 1-3\n")

                else:
                    egg = int(egg)
                    if egg == 1:
                        print("You have chosen dozen 1-12")
                    elif egg == 2:
                        print("You have chosen dozen 13-24")
                    elif egg == 3:
                        print("You have chosen dozen 25-36")
                    break


        elif btype == 5:
            print("You have chosen Straight Up!")
            while True:
                try:
                    one = input("Make your selection (any single number: 00 or 0-36): ")
                    if one == "00":
                        print(f"You have chosen {one}!")
                        one = 37
                        break
                    elif int(one) not in range(0, 37):
                        print("Please choose an option 00 or 0-36\n")
                    else:
                        print(f"You have chosen {one}!")
                        one = int(one)
                        break

                except ValueError:
                    print("Please choose an option 00 or 0-36\n")


        elif btype == 6:
            print("You have chosen Split!")
            while True:
                try:
                    split1 = input("Select the First number in your split bet (1-36): ")

                    if int(split1) > 36 or int(split1) < 1:
                        print("Please choose a number 1-36\n")
                    else:
                        split1 = int(split1)
                        break

                except ValueError:
                    print("Please choose a number 1-36\n")

            combos = []

            if split1 - 3 >= 1:
                combos.append(split1 - 3)
            if split1 + 3 <= 36:
                combos.append(split1 + 3)

            column = ((split1 - 1) % 3) + 1

            if column != 1:
                combos.append(split1 -1)
            if column != 3:
                combos.append(split1 + 1)

            if split1 == 1:
                combos.append(0)
            if split1 == 2:
                combos += [0, "00"]
            if split1 == 3:
                combos.append("00")

            neighbors = ""
            for i in combos:
                neighbors += (str(i) + ", ")
            neighbors = neighbors[:-2]

            while True:
                try:
                    split2 = input(f"Select the Second number in your split bet (options are: {neighbors}): ")
                    if split2 in combos and split2 != "00":
                        split2 = int(split2)
                    break

                except ValueError:
                    print(f"Please select from the possible adjacent numbers to {split1} ({neighbors})\n")

            print(f"You have placed your bet on the split {split1} and {split2}!")
            if split2 == "00":
                split2 = 37

        elif btype == 7:
            print("You have chosen Street!")
            while True:
                try:
                    street = int(input("Select your street (e.g., street 1 bets on 1, 2, and 3 while street 2 bets on 4, 5, 6): "))

                    if street not in range(1, 13):
                        print("Please select a street 1-12\n")
                    else:
                        base = [1, 2, 3]
                        for i in range(3):
                            base[i] += (3 * (street - 1))

                        print(f"You have chosen street {street}, your bet is for {base[0]}, {base[1]}, and {base[2]}!\n")
                        break

                except ValueError:
                    print("Please select a street 1-12\n")



        elif btype == 8:
            print("You have chosen Corner!")
            while True:
                try:
                    square = int(input("Select the starting corner number (e.g., selecting 10 bets on 10, 11, 13, and 14): "))
                    if 0 < square < 37:
                        print(f"You have chosen the corner {square}, your bet is on {square}, {square+1}, {square+3}, and {square+4} ")
                        break
                    else:
                        print("Please select a number from 1-32\n")

                except ValueError:
                    print("Please select a number from 1-32\n")

        elif btype == 9:
            print("You have chosen Basket!")
            basket = [0, 37, 1, 2, 3]
            print("The Basket bet is for 0, 00, 1, 2, and 3!")

        elif btype == 10:
            print("You have chosen Double Street!")
            while True:
                try:
                    dstreet = int(input("Select your double street (e.g., double street 1 bets on 1, 2, 3, 4, 5, 6 while double street 2 bets 4, 5, 6, 7, 8, 9 etc.): "))
                    if 0 < dstreet < 12:
                        dbase = [1, 2, 3]
                        for i in range(3):
                            dbase[i] += (3 * (dstreet - 1))
                        for i in range(1, 4):
                            dbase.append(i+dbase[2])
                        print(f"You have chosen street {dstreet}, your bet is for {dbase[0]}, {dbase[1]}, {dbase[2]}, {dbase[3]}, {dbase[4]}, and {dbase[5]}!")
                        break
                    else:
                        print("Please select a street from 1-11\n")

                except ValueError:
                    print("Please select a street from 1-11\n")







        while True:
            try:
                print()
                bet = int(input(f"Place your bet in chips (You have {chips} chips): " ))

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
        time.sleep(s)
        slot = random.randint(0, 37)


        if slot == 37: #GREEN
            print(f"The ball landed on slot 00 — GREEN!")
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


        time.sleep(t)

        if btype == 1:
            if c == color:
                print(f"Your selection of {color.lower()} was a Hit!\n")
                print(f"You won {bet} chips!")
                chips += bet
                token(chips, n)
            else:
                print(f"The ball did not land on {color.lower()}.\n")
                chips -= bet
                token(chips, n)

        elif btype == 2:
            if slot == 0:
                print(f"House Slot!")
                chips -= bet
                token(chips, n)

            elif slot == 37:
                print(f"House Slot!")
                chips -= bet
                token(chips, n)

            else:
                if slot % 2 == 0:
                    p = "EVEN"
                else:
                    p = "ODD"

                if parity == p:
                    print(f"Your selection of {parity.lower()} was a Hit!\n")
                    print(f"You won {bet} chips!")
                    chips += bet
                    token(chips, n)
                else:
                    print(f"The ball did not land in an {parity.lower()} pocket.\n")
                    chips -= bet
                    token(chips, n)

        elif btype == 3:
            m = ""
            if slot == 0:
                print(f"House Slot!")

            elif slot == 37:
                print(f"House Slot!")


            else:
                if slot in range(1, 19):
                    m = "LOW"
                elif slot in range(19, 37):
                    m = "HIGH"


            if magnitude == m:
                print(f"Your selection of {magnitude.lower()} was a Hit!\n")
                print(f"You won {bet} chips!")
                chips += bet
                token(chips, n)
            else:
                print(f"The ball did not land on a {magnitude.lower()} slot.\n")
                chips -= bet
                token(chips, n)

        elif btype == 4:
            e = ""
            if slot == 0:
                print(f"House Slot!")
            elif slot == 37:
                print(f"House Slot!")

            if egg == 1:
                choice = "1-12"
            elif egg == 2:
                choice = "13-24"
            elif egg == 3:
                choice = "25-36"

            if slot in range(1,13):
                e = 1
            elif slot in range(13, 25):
                e = 2
            elif slot in range(25-37):
                e = 3

            if egg == e:
                print(f"Your selection of the dozen {choice} was a Hit!\n")
                print(f"You won {bet * 2} chips!")
                chips += (bet * 2)
                token(chips, n)
            else:
                print(f"The ball did not land within the dozen {choice}.\n")
                chips -= bet
                token(chips, n)

        elif btype == 5:
            if slot == one:
                if one == 37:
                    one = "00"
                print(f"Your selection of {one} was a Hit!\n")
                print(f"You won {bet * 35} chips!")
                chips += (bet * 35)
                token(chips, n)
            else:
                if one == 37:
                    one = "00"
                print(f"The ball did not land on {one}.\n")
                chips -= bet
                token(chips, n)

        elif btype == 6:
            if slot == split1 or slot == split2:
                if split2 == 37:
                    slot = "00"
                print(f"Your selection of {slot} in the split was a Hit!\n")
                print(f"You won {bet * 17} chips!")
                chips += (bet * 17)
                token(chips, n)
            else:
                if split2 == 37:
                    split2 = "00"
                print(f"The ball did not land on {split1} or {split2}.\n")
                chips -= bet
                token(chips, n)

        elif btype == 7:
            if slot in base:
                print(f"Your selection of street {street} was a Hit!\n")
                print(f"You won {bet * 11} chips!")
                chips += (bet * 11)
                token(chips, n)
            else:
                print(f"The ball did not land in street {street}.\n")
                chips -= bet
                token(chips, n)

        elif btype == 8:
            if slot in [square, square + 1, square + 3, square +4]:
                print(f"Your selection of the {square}, {square+1}, {square+3}, and {square+4} was a Hit!\n")
                print(f"You won {bet * 8} chips!")
                chips += (bet * 8)
                token(chips, n)
            else:
                print(f"The ball did not land in any of the corners on the square.\n")
                chips -= bet
                token(chips, n)

        elif btype == 9:
            if slot in basket:
                print(f"The ball landed in the basket!\n")
                print(f"You won {bet * 6} chips!")
                chips += (bet * 6)
                token(chips, n)
            else:
                print(f"The ball did not land in the basket.\n")
                chips -= bet
                token(chips, n)

        elif btype == 10:
            if slot in dbase:
                print(f"Your selection of double street {dstreet} was a Hit!\n")
                print(f"You won {bet * 5} chips!")
                chips += (bet * 5)
                token(chips, n)
            else:
                print(f"The ball did not land in double street {dstreet}.\n")
                chips -= bet

                token(chips,n)


