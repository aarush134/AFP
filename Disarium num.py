# Disarium Number - Lesson 135: Python Refresher

num = input("Enter a number: ")
total = 0

for i in range(len(num)):
    digit = int(num[i])
    total += digit ** (i + 1)

if total == int(num):
    print(f"{num} is a Disarium number! ✅")
else:
    print(f"{num} is NOT a Disarium number ❌")
