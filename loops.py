# Exercise 1: Add numbers until the user enters a negative number

total = 0

while True:
    number = float(input("Enter a number, or a negative number to stop: "))

    if number < 0:
        break

    total += number

print(f"The total is: {total}")