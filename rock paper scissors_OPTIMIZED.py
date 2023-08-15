import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]

playerOption = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

if playerOption < 0 or playerOption > 2:
    print("Invalid input. Please choose 0, 1, or 2.")
else:
    cpuOption = random.randint(0, 2)

    print("Player chose:")
    print(choices[playerOption])

    print("CPU chose:")
    print(choices[cpuOption])

    if playerOption == cpuOption:
        print("It's a draw!")
    else:
        win_conditions = {
            (0, 2): "Player wins!",
            (2, 1): "Player wins!",
            (1, 0): "Player wins!",
            (2, 0): "CPU wins!",
            (1, 2): "CPU wins!",
            (0, 1): "CPU wins!"
        }

        if (playerOption, cpuOption) in win_conditions:
            print(win_conditions[(playerOption, cpuOption)])
