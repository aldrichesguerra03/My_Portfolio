print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

lower_case_name1 = name1.lower()
lower_case_name2 = name2.lower()


name1_true = lower_case_name1.count("t") + lower_case_name1.count("r") + lower_case_name1.count("u") + lower_case_name1.count("e")

name2_true = lower_case_name2.count("t") + lower_case_name2.count("r") + lower_case_name2.count("u") + lower_case_name2.count("e")

total_true = name1_true + name2_true

name1_love = lower_case_name1.count("l") + lower_case_name1.count("o") + lower_case_name1.count("v") + lower_case_name1.count("e")

name2_love = lower_case_name2.count("l") + lower_case_name2.count("o") + lower_case_name2.count("v") + lower_case_name2.count("e")

total_love = name1_love + name2_love

true_love = int(str(total_true) + str(total_love))

if true_love < 10 or true_love > 90:
    print(f"Your score is {true_love}, you go together like coke and mentos.")
elif true_love > 40 and true_love <50:
    print(f"Your score is {true_love}, you are alright together.")
else:
    print(f"Your score is {true_love}.")








  

