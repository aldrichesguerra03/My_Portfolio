print("Welcome to the tip calculator!")
total_bill = input("What was the total bill? $")

tip = input("How much tip would you like to give? 10, 12, or 15?  ")

people = input("How many people to split the bill? ")

total_bill_int = float(total_bill)
tip_int = int(tip)
people_int = int(people)

computation_tip = tip_int / 100
computation_bill = total_bill_int * computation_tip
actual_bill = total_bill_int + computation_bill



result = "{:.2f}".format(actual_bill / people_int)



print(f"Each person should pay ${result}.")











