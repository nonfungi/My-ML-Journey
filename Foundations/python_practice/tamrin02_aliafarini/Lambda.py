#1-------------------------------------------------------
#Sort a list of tuples [(name, age)] by age using sorted with a lambda key.

people = [('ali', 32), ('reza', 25), ('sara', 29), ('neda', 22)]
sorted_people = sorted(people, key=lambda person: person[1])
print(f"Sorted by age: {sorted_people}")


#2-------------------------------------------------------
#Given prices = [120, 55, 300, 90], use a lambda with map to apply a 10% discount to all prices and return the new list.

prices = [120, 55, 300, 90]
discount_prices = list(map(lambda item: item * 0.9, prices))
print (f"Prices after 10% discount: {discount_prices}")


#3-------------------------------------------------------
#Given a list of strings, sort them by their last character using a lambda with sorted.

list_of_strings = input("enter a list of strings separated by spaces: ").split()
sort_by_last_char = sorted(people, key=lambda s: s[-1])
print(f"Sorted by last character: {sort_by_last_char}")