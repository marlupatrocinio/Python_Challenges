from replit import clear
#HINT: You can call clear() to clear the output in the console.
bids = {}

def addBids():
  name = input("What is your name? ")
  bidValue = int(input("What is your bid? $"))
  bids[name] = bidValue

def findHighestBid(biddingRecord):
  highestBid = 0
  for bidder in biddingRecord:
    bidAmount = biddingRecord[bidder]
    if bidAmount > highestBid:
      highestBid = bidAmount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highestBid}")

addBids()

option = input("Are there other users who want to bid? answer with yes or no: ")

while option.lower() == "yes":
  clear()
  addBids()
  option = input("Are there  other users who want to bid? answer with yes or no: ")

findHighestBid(bids)