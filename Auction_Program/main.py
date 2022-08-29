from art import logo

bids = []
highest_bid = 0
bidder_name = ""
auction_list = {}

def auction_adder(name, bid):
    auction_list[name] = bid

print(logo)
auction_program = True
while auction_program:
    name_input = input("What is your name?\n")
    bid_price = int(input("What is your bid price?\n"))
    auction_adder(name_input, bid_price)
    new_bidder = input("Is there another bidder who wants to bid? Type 'y' if yes and 'n' if no\n")

    if new_bidder == 'n':
        auction_program = False

for bidder in auction_list:

    if auction_list[bidder] > highest_bid:
        highest_bid = auction_list[bidder]
        bidder_name = bidder

print(f"The winner is {bidder_name} with the bid of ${highest_bid}.")



