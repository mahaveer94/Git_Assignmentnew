# Simple Python program to print a pattern

def print_pattern(n):
    """
    Function to print the pattern
    """
    for i in range(1, n + 1):
        print("*" * i)

# Get the number of rows from the user
num_rows = int(input("Enter the number of rows: "))

# Call the function to print the pattern
print_pattern(num_rows)