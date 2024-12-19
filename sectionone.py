# This program prints the numbers from 1 to 100 with some special rules.
# For multiples of 3, it prints "Fizz" instead of the number.
# For multiples of 5, it prints "Buzz" instead of the number.
# For numbers that are multiples of both 3 and 5, it prints "FizzBuzz".

# Loop through numbers from 1 to 100
for i in range(1, 101):
    # Check if the number is a multiple of both 3 and 5
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    # Check if the number is a multiple of 3
    elif i % 3 == 0:
        print("Fizz")
    # Check if the number is a multiple of 5
    elif i % 5 == 0:
        print("Buzz")
    # If the number is not a multiple of 3 or 5, print the number itself
    else:
        print(i)