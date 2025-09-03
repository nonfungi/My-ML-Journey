# The function to safely divide list elements
# Write a function safe_divide_list(nums, d) that divides each number in nums by d. 
# Use a loop and try/except to handle division by zero and non-numeric values; return a new list where invalid divisions are replaced with None.



def safe_divide_list(nums, d):
    results = []
    # Loop through each item in the list
    for num in nums:
        # Try to perform the conversion and division
        try:
            result = float(num) / d
            results.append(result)
        except (ValueError, ZeroDivisionError):
            results.append(None)
    return results

nums = input("Enter a list of numbers separated by spaces: ").split()

# Try to get a valid divisor from the user
try:
    d_input = input("Enter a divisor: ")
    d = float(d_input)
    print(f"Results: {safe_divide_list(nums, d)}")
except ValueError:
    print(f"Error: Invalid input for the divisor. '{d_input}' is not a valid number.")




#2-------------------------------------------------------
# Write a function read_int_until_valid(prompt) that loops asking the user for an integer and 
# uses try/except to keep asking until a valid integer is entered. Return the integer.


def read_float_until_valid(prompt):
    while True:
        try:
            unvalid_input = input(prompt)
            int_prompt = float(unvalid_input)
            return int_prompt
        except ValueError:
            print(f"Error: Invalid input. '{unvalid_input}' is not a valid number please try another one.")
age = read_float_until_valid("Enter your age: ")
print(f"Your age is: {age}")
weight = read_float_until_valid("Enter your weight: ")
print(f"Your weight is: {weight}")

#3-------------------------------------------------------
# Implement sum_valid_numbers(text_values) that loops over a list like ["10", "abc", "3.5", "7"]
#  and sums only the valid numeric entries (ints or floats). Use try/except.


def sum_valid_numbers(text_values):
    total = 0
    for value in text_values:
        try:
            num = float(value)
            total += num
        except ValueError:
            continue
    return total
text_values = input("Enter a list of numbers separated by spaces: ").split()
print(f"The sum of valid numbers is: {sum_valid_numbers(text_values)}")




