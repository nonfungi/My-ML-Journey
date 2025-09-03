#Python Assignments
#----------------------------------------------------------------------------------------
#####1. Variables
#Questions
#1. Store your name, age, and favorite color in variables and print them.

my_name = 'ali'
my_age = 31
favorite_color = 'yellow'
print(f"my name is {my_name}, my age is {my_age}, my favorite color is {favorite_color}")

#2. Swap the values of two variables without using a third variable.

a = 5
b = 10  
a, b = b, a

#3. Calculate the area of a rectangle using the variables length and width.

length = 7
width = 4
area = length * width
#----------------------------------------------------------------------------------------   
#####2. Input & Output
#Questions
#1. Ask the user for their name and age, then print: Hello Ali, you are 20 years old.

print(f"hello {input('Enter your name: ')}, you are {input('Enter your age: ')} years old.")

#2. Ask the user for two numbers and print their sum, difference, product, and division.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))    
print(f"Sum: {num1 + num2}, Difference: {num1 - num2}, Product: {num1 * num2}, Division: {num1 / num2}")

#3. Ask the user for their birth year and print their age (assume the current year is 2025).

print(f"your age is {2025- int(input("enter your birthday year:"))}")

