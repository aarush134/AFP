# Find the value - Lesson 134: Dictionaries and Tuples

# Predefined dictionary
info = {
    "name": "Aarush",
    "age": 13,
    "hobby": "Coding",
    "language": "Python",
    "homie": "ChatGPT"
}

# Ask user for a key
key = input("Enter the key you want to search (e.g., name, age): ")

# Display result
if key in info:
    print(f"The value for '{key}' is: {info[key]}")
else:
    print("Key not found in dictionary.")
