import os
from art import logo


# Initial print logo
print(logo)

# Creat a dictionary contain names as key and bid as value
bid_table = {}
other_bid = False # when there is still someone to bid

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# initial highest bid and person with highest bid
def find_the_winner(bidding_record):
  
  highest_bid = 0
  person_with_highest_bid = ""

  for person in bid_table:
    if bid_table[person] > highest_bid:
        highest_bid = bid_table[person]
        person_with_highest_bid = person
  print(f"{person_with_highest_bid} has won with {highest_bid} bid.")
  
# add_new function: take name and bid of one person and add to bid_table dictionary

def add_new(name, bid):
  bid_table[name] = bid

# Run a loop to grab bidder

while not other_bid:


  name = input("What's your name?? ").lower()
  bid = int(input("What's your bid? "))

  # call add_new to add new bider
  add_new(name, bid)

  # check if there is someone wants to join
  should_continue = input("Is there anyone else want to join? Type y(Yes) or n(No)\n").lower()
  
  ### If no other bider
  # Iterate through the dictionary to find the highest bid
  if should_continue == "n":
    other_bid = True
    find_the_winner(bid_table)
  ## clear screen if still someone
  elif should_continue == "y":
    clear()
    print(logo)
    




