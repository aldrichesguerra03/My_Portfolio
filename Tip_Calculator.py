#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

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











