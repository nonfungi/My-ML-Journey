#####5. Functions
#Questions
#1. Write a function that takes two numbers and returns their sum.
def sum(a,b):
    return a+b

print(f"sum is :{sum(int(input('enter a: ')), int(input('enter b: ')))}")

#2. Write a function that takes a list of numbers and returns the largest number.

def largest_number():
    numbers = [int(x) for x in input("enter numbers separated by space: ").split()]
    return max(numbers) 

print(f"largest number is :{largest_number()}")

#3. Write a function that takes a string and returns the number of vowels in it.

vowels = "aeiouAEIOU"
def count_vowels(s):
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
print(f"number of vowels is :{count_vowels(input('enter a string: '))}")

