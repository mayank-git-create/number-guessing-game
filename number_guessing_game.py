# The Number Game #Python3
import random
import time

print("Welcome to the Number Guessing Game by Martin Thong.")
print("Hope you have fun!!!")
players = input("Enter the number of players: ")
while players.isdigit() != True:
    print("You have key in an invalid number")
    players = input("Enter the number of players: ")
players = int(players)

winner_rounds = input("The overall winner has to win how many rounds?: ")
while winner_rounds.isdigit() != True:
    print("You have key in an invalid number")
    winner_rounds = input("he overall winner has to win how many rounds?:")
winner_rounds = int(winner_rounds)

winnings = []  # store the number of winnings by each player
nameList = []  # store the names of the players

# creating the list for all the players
for i in range(players):
    winnings.append(0)
    name = input("Enter player " + str(i + 1) + " name: ")
    nameList.append(name)
round = 99  # game should end before this
print
for r in range(round):
    guessCount = []  # store the number of guess by each player
    for i in range(players):
        guessCount.append(0)
    high = 100
    low = 0
    print("-" * 15 + "ROUND " + str(r + 1) + "-" * 15)
    secretNumber = random.randint(1, 99)
    # print secretNumber
    # guessCount = guessCountList #reset guesses for each round
    # print guessCount
    playerNumber = 1
    guess = input(
        nameList[playerNumber - 1]
        + " - Enter a number between "
        + str(low)
        + " and "
        + str(high)
        + ": "
    )
    guessCount[playerNumber - 1] = guessCount[playerNumber - 1] + 1
    while guess != str(secretNumber):
        if guess.isdigit():
            guess = int(guess)
            if guess >= low and guess <= high:
                if guess < secretNumber:
                    low = guess
                    print(nameList[playerNumber - 1] + ", your guess is too low!")
                else:
                    high = guess
                    print(nameList[playerNumber - 1] + ", your guess is too high!")
            else:
                print(nameList[playerNumber - 1] + ", the number out of range!")
        else:
            print(nameList[playerNumber - 1] + ", only number is allowed!")
        if playerNumber < players:
            playerNumber = playerNumber + 1
        else:
            playerNumber = 1
        guess = input(
            nameList[playerNumber - 1]
            + " - Enter a number between "
            + str(low)
            + " and "
            + str(high)
            + ": "
        )
        guessCount[playerNumber - 1] = guessCount[playerNumber - 1] + 1

    print("-" * 15 + "Congratulations!!!" + "-" * 15)
    winnings[playerNumber - 1] = winnings[playerNumber - 1] + 1
    print(nameList[playerNumber - 1] + ", you made the right guess!")
    print("The secret number is " + str(secretNumber))

    for i in range(players):
        print(nameList[i] + " - Total number of wins: " + str(winnings[i]))
    print
    maxWin = max(winnings)
    winPlayer = winnings.index(max(winnings))
    # print maxWin
    # print winnings.count(maxWin)
    # print winner_rounds
    if maxWin == (winner_rounds):
        print("HURRAY! The overall winner is " + nameList[winPlayer])

        break

print
print("Thanks for playing!")
print("Signed off, Martin Thong...")
time.sleep(5)
