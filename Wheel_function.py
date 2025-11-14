import time
import random
def RouletteWheel():
    maxdelay = random.uniform(1, 1.3)
    start = 0
    slot = random.randint(0, 37)
    wheel = [
        0,
        28, 9, 26, 30, 11, 7, 20, 32, 17,
        5, 22, 34, 15, 3, 24, 36, 13, 1,
        37,  # 00
        27, 10, 25, 29, 12, 8, 19, 31, 18,
        6, 21, 33, 16, 4, 23, 35, 14, 2
    ]

    while True:
        pocket = str(wheel[slot])
        if int(pocket) in [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]:  # RED
            print(f"\033[1;31m{pocket}")

        elif int(pocket) in [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]:  # BLACK
            print(f"\033[1;30m{pocket}")

        elif int(pocket) == 0:  # GREEN
            print(f"\033[1;32m0")

        elif int(pocket) == 37:
            print(f"\033[1;32m00")

        slot += 1
        if slot == 38:
            slot = 0

        t = start/59
        delay = .01 + ((.99) * (t**2.7))
        time.sleep(delay)
        start += 1

        if delay > maxdelay:
            print(f"\033[0m", end="")
            return pocket

if __name__ == "__main__":
    print(f"\033[1mThe ball landed on {RouletteWheel()}!")

