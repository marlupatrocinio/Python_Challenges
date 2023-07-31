print("Welcome to the tip calculator.")

bill = float(input("What was the total bill?"))
percentageTip = int(input("What percentage tip would you like to give? 10, 12 or 15?"))
people = int(input("How many people to split the bill?"))

percentage = percentageTip / 100

total = bill * percentage

finalBill = bill + total

split = finalBill / people

totalEachPerson = round(split, 2)

print (f"Each person should pay ${totalEachPerson}")