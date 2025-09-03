user = input("Enter username: ")
city = input("Enter city: ")

with open("profile.txt", "w") as file:
    file.write(f"Username: {user}\n")
    file.write(f"City: {city}\n")



with open("profile.txt", "r") as file:
    file.readline()  # Skip the first line
    print(f"welcome back,{}")