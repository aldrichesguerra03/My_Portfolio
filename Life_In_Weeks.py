# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

age_for_days = 90 - int(age)
age_for_weeks = 90 - int(age)
age_for_months = 90 - int(age)

age_for_days *= 365
age_for_weeks *= 52
age_for_months *= 12



print(f"You have {age_for_days} days, {age_for_weeks} weeks, and {age_for_months} months left.")
