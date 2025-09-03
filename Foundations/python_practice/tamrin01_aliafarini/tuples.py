#####4. Tuples

#Questions
#1. Create a tuple of 5 colors. Print the first and last elements

colors = ("red", "blue", "green", "yellow", "purple")
print(colors[0], colors[-1])

#2. Write a program that converts a list into a tuple.
my_list = [1, 2, 3, 4, 5]
my_tuple = tuple(my_list)


#

numbers = (10, 20, 10, 40, 10, 40)
print(f"the tuple is {numbers}")
x = int(input("enter the number you want to count:"))
count = numbers.count(x)
print(f"the count of {x} is {count}")

