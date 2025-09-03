#Loops
#Write a program that prints all even numbers from 1 to 100 using a for loop.
even = []
for i in range (100):
    if i%2 == 0:
        even.append(i)
print (even)


#2
#Using a while loop, ask the user to enter numbers until they type 0. Print the sum of all entered numbers (excluding 0).

entered_number = []
while i != 0:
    i = int(input("Enter a number (0 to stop): "))
    entered_number.append(i)

print("You entered:", entered_number)

#3
#Print the multiplication table for a number n (from 1 to 10), where n is input by the user.

my_list = list(range(11))
n = int(input("enter a number in (0 to 10): "))
if n in my_list:
    for i in my_list:
        print (i*n)