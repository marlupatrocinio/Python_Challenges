import random

def dealCard():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

user = []
cpu = []
user.append(dealCard())
user.append(dealCard())
cpu.append(dealCard())
cpu.append(dealCard())

userScore = sum(user)
cpuScore = sum(cpu)

print(user, cpu)
print(userScore, cpuScore)
endGame = False

while endGame == False:
  if userScore or cpuScore == 21:
    if userScore == 21:
      print("User blackJack, you win!")
      endGame = True
    elif cpuScore == 21:
      print("Cpu blackJack, you lose!")
      endGame = True
  elif userScore or cpuScore > 21:
    if userScore > 21:
      print("You lose!")
      endGame = True
    else:
      print("You win!")
      endGame = True
  
  option = input("Do you want to get another card? type yes or no")
  if option == "yes":
    user.append(dealCard())
    print(user)
  
userScore = sum(user)

print(user, cpu)
print(userScore, cpuScore)
