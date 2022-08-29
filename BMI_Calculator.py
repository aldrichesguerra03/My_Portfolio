height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

new_height = float(height)
new_weight = int(weight)

bmi = new_weight / new_height ** 2

result =  int(bmi)

print(result)

