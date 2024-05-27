from codecs import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)

bids={}

bid_finished=False

def highest_bidder(bidding_record):
  highest_bid=0
  for bidder in bidding_record:
    bid_amt=bidding_record[bidder]
    if bid_amt>highest_bid:
      highest_bid=bid_amt
      winner=bidder
  print(f"The winner is {winner} with highest bid of ${highest_bid}")



      
while not bid_finished:
  name=input("What is the name of the bidder?: ")
  bid_price=int(input("What is your bid price?: $"))
  
  bids[name]=bid_price
  others=input("Are ther opther users who want to bid?: ")



  if others=="no":
    bid_finished=True
    highest_bidder(bids)
  elif others=="yes":
    clear()
   