for numbers in range(1, 101):
    if numbers % 15 == 0:
        numbers = "FizzBuzz"
    elif numbers % 5 == 0:
        numbers = "Buzz"
    elif numbers % 3 == 0:
        numbers = "Fizz"

    print(numbers)