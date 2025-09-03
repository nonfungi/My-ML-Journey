#1---------------------------------------------------------
# From a list of email strings, use filter to keep only those that contain exactly one '@' and at least one dot after the '@'.



def is_prime (n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
prime = []

for i in range(100):
    if is_prime(i):
        prime.append(i) 
print(prime)

#2-------------------------------------------------------
# Write a function count_occurrences(items, target) that returns how many times target appears in the list items.

#def count_occurrences(items, target):
#    count = 0
#    for item in items:
#        if item == target:  
#            count += 1
#    return count    

items = []
while True:  
    user_input = input("Enter a number (or 'stop' to finish) to make a list: ")
    if user_input == 'stop':
        break 
    num = int(user_input)
    items.append(num)

target = int(input("Now enter your target number to count: "))
result = items.count(target)
print(f"The number {target} appears {result} times in the list.")


#3-----------------------------------------------------
# Write a function normalize_scores(scores) that takes a list of numbers and returns a new list scaled to 0–100 
# (divide by max and multiply by 100). Handle an empty list by returning an empty list.

def normalize_scores(scores):
    if not scores:
        return []
    max_value = max(scores)
    normalized_list = []
    for i in range(len(scores)):
        normalized_list.append( (scores[i] / max_value) * 100 )
    return normalized_list
list_scores = []
while True:
    user_input = input("Enter a score for normalize (or 'stop' to finish): ")
    if user_input.lower() == 'stop':
        break
    try:
        list_scores.append(int(user_input)) 
    except ValueError:
        print("Invalid input. Please enter a valid number or 'stop'.")          

print(f"your normalized_scores is: {normalize_scores(list_scores)}")



