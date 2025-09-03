#####3. Lists
#Questions
#1. Create a list of 5 fruits and print the second and last fruit.

fruits = ["apple", "banana", "cherry", "orange", "berry"]
print(fruits[1], fruits[-1])

#2. Ask the user to enter 5 numbers and store them in a list. Print the maximum and minimum.

numbers = []
for i in range(5):
    numbers.append(int(input("enter a number:")))

print(f"maximum number is {max(numbers)},  and minimum number is {min(numbers)}")


#3. Write a program that removes duplicates from a list.
items = [1, 2, 2, 3, 4, 4, 5]
unique_items = set(items)
print(unique_items)


