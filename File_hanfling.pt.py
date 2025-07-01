# File Handling - Operations Part 2

# Create and write to a file
with open("my_file.txt", "w") as file:
    file.write("Hello, this is a sample file.\n")
    file.write("Python file handling is fun!\n")

# Read the file
with open("my_file.txt", "r") as file:
    print("Reading the file content:")
    print(file.read())

# Append new data
with open("my_file.txt", "a") as file:
    file.write("Adding more lines to the file...\n")

# Read again to verify appending
with open("my_file.txt", "r") as file:
    print("\nAfter appending:")
    print(file.read())
