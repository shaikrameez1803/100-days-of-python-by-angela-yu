##****BLIND AUCTION PROJECT****########
from random import choice
action_running=True
items={}
while action_running==True:
    name=(input("What is your name?:"))
    price=float(input("What is your bid?: $"))
    items[name]=price
    choice=input('If there are other users who want to bid?-"Yes" or "No":').lower()
    if choice=="yes":
        print("\n"*50)
        action_running=True
    else:
            action_running=False

highest_bid=0
winner=""
for name,price in items.items():
    if price>highest_bid:
        highest_bid=price
        winner=name
print(f"The winner is {winner} with a bid of ${highest_bid}")