#TIP CALCULATOR PROJECT#
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tip_percentage=tip%100
bill_with_tip=((bill/tip_percentage)+bill)
final_bill=float(bill_with_tip/people)
final_amount = round(final_bill, 2)
print(f"Each person should pay: ${final_amount}")





