#1-------------------------------------------------------
#Using functools.reduce, compute the product of all numbers in a list (e.g., [2,3,4] -> 24).

from functools import reduce


my_list = input("Enter a list of numbers separated by spaces: ").split()
my_list = list(map(int, my_list))
product = reduce(lambda x, y: x* y, my_list)
print(f"The product of all elements in the list is: {product}")


#2-------------------------------------------------------
#Using reduce, find the longest string in a list of strings.

try:

    list_of_strings = input("enter a list of strings to find the longest one (separated by spaces): ").split()
    list_of_strings = reduce(lambda x, y: x if len(x) > len(y) else y, list_of_strings)

except ValueError:
    print("Invalid input. Please enter a valid list of strings separated by spaces.")
    pass    
print(f"The longest string in the list is: {list_of_strings}")



#3-------------------------------------------------------
#Using reduce, concatenate a list of words into a sentence separated by spaces (avoid a leading/trailing space).

before_concatenate = input("enter a list of strings to concatenate separated by spaces: ").split()
concatenate_string = reduce(lambda accumulator, next_word: accumulator + " " + next_word, before_concatenate)
print(f"Concatenated string: {concatenate_string}")