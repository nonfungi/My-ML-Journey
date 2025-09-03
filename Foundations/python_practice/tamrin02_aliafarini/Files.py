#Files in Python
# Ask the user for a filename, then append a new line containing the current date and time to that file. If the file doesn’t exist, create it.

from datetime import datetime

# Get the filename from the user
filename = input("Enter the filename (e.g., log.txt): ")
# Format the current time for appending
current_time = datetime.now()
timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S") + "\n"

# --- Step 1: Append to the file (same as before) ---
try:
    with open(filename, 'a') as f:
        f.write(timestamp)
    print(f"Successfully appended the date and time to {filename}")

    # --- Step 2: Read and display the file's content ---
    print("-" * 20) # Add a separator for clarity
    print(f"Content of '{filename}':")
    with open(filename, 'r') as f:
        content = f.read() # Read the entire file into a string
        print(content)

except IOError as e:
    print(f"Error: Could not access file {filename}. Reason: {e}")



#2-------------------------------------------------------
# Given a text file of numbers (one per line), read the file and compute the average. Handle empty files and invalid lines gracefully.
total_sum = 0
valid_number_count = 0

try:
    with open('numbers.txt', 'r') as f:
        for line in f:
            try:
                numbers = float(line.strip())
                total_sum += numbers
                valid_number_count += 1
            except ValueError:
                continue
    if valid_number_count > 0:
        average = total_sum / valid_number_count
        print(f"The average of valid numbers is: {average}")
    else:
        print("No valid numbers found in the file.")
except FileNotFoundError:
    print("Error: The file 'numbers.txt' does not exist.")

#3-------------------------------------------------------
# Write a program that copies the contents of input.txt to output.txt, but only lines that are not empty and don’t start with #.
 # You can read from 'input_file' and write to 'output_file' here.
with open('input.txt', 'r') as input_file, open('output.txt', 'w') as output_file:
    for line in input_file:
        stripped_line = line.strip()
        if stripped_line and not stripped_line.startswith('#'):
            output_file.write(line)
print("File has been copied and filtered successfully!")