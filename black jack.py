import random

def dealCard():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def checkScore(userScore, cpuScore):

    if userScore == 21:
        print("User blackJack, you win!")
        return True
    elif cpuScore == 21:
        print("Cpu blackJack, you lose!")
        return True
    elif userScore > 21:
        print("You lose!")
        return True
    elif cpuScore > 21:
        print("You win!")
        return True
    return False

user = []
cpu = []
user.append(dealCard())
user.append(dealCard())
cpu.append(dealCard())
cpu.append(dealCard())

userScore = sum(user)
cpuScore = sum(cpu)

print(user, cpu)
print("User Score:", userScore)
endGame = False

while not endGame:
    option = input("Do you want to get another card? type yes or no: ")
    if option == "yes":
        user.append(dealCard())
        userScore = sum(user)
        print("User drew a card:", user[-1])
    elif option == "no":
        if not endGame:
            while cpuScore < 17:
                cpu.append(dealCard())
                cpuScore = sum(cpu)
                print("CPU drew a card:", cpu[-1])

    endGame = checkScore(userScore, cpuScore)
    print(user)
    print("User Score:", userScore)
    print(cpu)
    print("CPU Score:", cpuScore)
