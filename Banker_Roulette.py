import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

names_length = len(names)

random_choice = random.randint(0, names_length - 1)

list_names = names[random_choice]

print(list_names + " is going to buy the meal today!")


