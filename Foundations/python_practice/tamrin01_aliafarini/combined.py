#####Mini-Project: Shopping List Manager

#2. Ask the user how many items they want to add.
#3. Input each item's name and price.
#4. Store them in a list of tuples (item_name, price).
#5. Functions: display all items, calculate total cost, find the most expensive item.
number_of_items = input("welcome to shopping list manager, how many items do you want to add?")

list_of_items = []

def calculate_total(items):
    total = 0
    for item in items:
        total += item[1]
    return total

for i in range(int(number_of_items)):
    item_name = input(f"enter the name of item {i+1}: ")
    item_price = float(input(f"enter the price of item {i+1}: "))
    item_tuple = (item_name, item_price)
    list_of_items.append(item_tuple)
print(f"your shopping list is :{list_of_items}, and te total cost is :{calculate_total(list_of_items)}")

