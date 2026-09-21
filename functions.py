# Exercise 1: Calculate the average of a list of scores

def calculate_average(numbers):
    return sum(numbers) / len(numbers)


scores = [72, 88, 55, 91]
average_score = calculate_average(scores)

print(f"The average score is: {average_score:.2f}")
