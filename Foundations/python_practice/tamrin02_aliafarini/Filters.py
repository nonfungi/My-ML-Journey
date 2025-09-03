###filters
#1-------------------------------------------------------
# Given a list of integers, use filter to keep only the positive numbers.


list_of_integers = input("enter a list of integers separated by spaces: ").split()
list_of_integers = list(map(int, list_of_integers))
list_of_positive_integer = list(filter(lambda x: x>=0, list_of_integers))
print(f"your positive number is: {list_of_positive_integer}")


#2-------------------------------------------------------
# From a list of words, use filter to keep only those with length ≥ 5.

list_of_words = input("enter a list of words separated by spaces: ").split()
list_of_words_length5 = list(filter(lambda x: len(x)>4, list_of_words))
print(list_of_words_length5)

#3-------------------------------------------------------
# From a list of email strings, use filter to keep only those that contain exactly one '@' and at least one dot after the '@'.

list_of_emails = input("enter a list of emails separated by spaces: ").split()
list_of_emails = list(filter(lambda x: "@" in x and "." in x, list_of_emails))
print(list_of_emails)