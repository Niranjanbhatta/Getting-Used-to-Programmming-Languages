import os
bids = {}

def highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")
        
new_bidder = False
while not new_bidder:
    name = input("Enter your name ")
    bid = int(input("Enter your bid $"))
    bids[name] = bid
    should_continue = input("Are there any new bidder")
    if should_continue == "no":
        new_bidder = True
        highest_bidder(bids)
    elif should_continue == "yes":
        os.system('cls')
