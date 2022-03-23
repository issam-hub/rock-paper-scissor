import random
import time

values = ["rock", "paper", "scissor"]

lose_count = 0
win_count = 0

tries = 0

print("welcome to rock, paper, scissor game !".capitalize().center(52, "*"))
print("*" * 52)
while tries < 3:
    print("(1) rock")
    print("(2) paper")
    print("(3) scissor")
    inp = int(input("enter your choice: ").strip())

    if inp not in range(1, 4):
        raise Exception("choose between 1 till 3")

    print("the computer choice is: ")
    for itr in range(1, 4):
        time.sleep(1)
        print(f"{itr}...")

    pcChoice = values[random.randint(0,2)]

    print(f">> {pcChoice}")

    print("*"*40)

    if inp == 1 and pcChoice == "paper":
        print("lose :(")
        lose_count += 1
    elif inp == 2 and pcChoice == "rock":
        print("win :)")
        win_count += 1
    elif inp == 1 and pcChoice == "scissor":
        print("win :)")
        win_count += 1
    elif inp == 3 and pcChoice == "rock":
        print("lose :(")
        lose_count += 1
    elif inp == 2 and pcChoice == "scissor":
        print("lose :(")
        lose_count += 1
    elif inp == 3 and pcChoice == "paper":
        print("win :)")
        win_count += 1
    elif inp == values.index(pcChoice)+1:
        print("draw")

    print(f"pc count: {lose_count}")
    print(f"win count: {win_count}")

    tries += 1
    print("*"*40)

if lose_count > win_count:
    print("looser, try again next time")
elif lose_count < win_count:
    print("what a win, yaaaay")
else:
    print("faire play, 🤝")