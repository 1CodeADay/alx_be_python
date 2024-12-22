
# Prompt the user for the pattern size
size = int(input("Enter the size of the pattern: "))

# Validate the input
if size <= 0:
    print("Please enter a positive integer.")
else:
    # Use a while loop for rows
    row = 0
    while row < size:
        # Use a for loop for columns
        for col in range(size):
            print("*", end="")  # Print '*' without moving to a new line
        print()  # Move to the next row
        row += 1
