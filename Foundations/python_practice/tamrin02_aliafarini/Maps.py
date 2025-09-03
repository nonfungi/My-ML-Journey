### Maps.py
#1-------------------------------------------------------
#Given a list of names like ["ali", "Sara", "omid"], use map to return a new list with each name capitalized (first letter uppercase, rest lowercase).


names = ["sara", "ali", "reza"]

def capitalized_names():
    return list(map(str.capitalize , names))
print(capitalized_names())


#2-------------------------------------------------------
#Given a list of Celsius temperatures, use map to convert them to Fahrenheit using the formula F = C * 9/5 + 32 .
temperatures_celsius = []

while True:
    try:
        user_input = input("Enter a temp (or 'stop' to finish): ")
        if user_input.lower() == 'stop':
            break   
        temperatures_celsius.append(float(user_input))
    except ValueError:
        print("Invalid input. Please enter a valid number or 'stop'.")
        pass    

print("Celsius to Fahrenheit:", list(map(lambda c: (c * 9/5) + 32, temperatures_celsius)))

#3-------------------------------------------------------
#Use map to transform a list of strings ["1","2","3","-4"] into integers. Filter out any values that cannot be converted 
# (hint: use a helper function that returns None on failure and then remove None later).

def is_integer(s):
    try:
        int(s)
        return True 
    except ValueError:
        return None

list_of_strings = ["3", "5", "2", "0", "-4", "hasan"]
list_of_integers = list(filter(is_integer, list_of_strings))
list_of_integers = list(map(int, list_of_integers))

print(list_of_integers)
