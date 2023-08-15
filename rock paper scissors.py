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

import random

playerOption = int(
    input(
        "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"
    ))

cpuOption = random.randint(0, 2)

Rock = 0
Paper = 1
Scissors = 2

if playerOption == 0:
    print("Player chose rock: " + rock)
if playerOption == 1:
    print("Player chose paper: " + paper)
if playerOption == 2:
    print("Player chose scissors: " + scissors)

print("-------------------------------------------------")

if cpuOption == 0:
    print("CPU chose rock: " + rock)
if cpuOption == 1:
    print("CPU chose paper: " + paper)
if cpuOption == 2:
    print("CPU chose scissors: " + scissors)

print("-------------------------------------------------")

if playerOption == 0 and cpuOption == 2:
    print("Player wins!")

if cpuOption == 0 and playerOption == 2:
    print("CPU wins!")

if playerOption == 2 and cpuOption == 1:
    print("Player wins!")

if cpuOption == 2 and playerOption == 1:
    print("CPU wins!")

if playerOption == 1 and cpuOption == 0:
    print("Player wins!")

if cpuOption == 1 and playerOption == 0:
    print("CPU wins!")

if playerOption == cpuOption:
    print("it's a draw!")
