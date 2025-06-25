f = open('students.txt', 'w')
f.write("Roy - Favorite Subject: Math\n")
f.close()

f = open('students.txt', 'a')
f.write("Sita - Favorite Subject: Science\n")
f.close()

f = open('students.txt', 'r')
print(f.read())
f.close()

f = open('students.txt', 'r+')
f.write("Updated Roy - Favorite Subject: Computer Science\n")
f.close()
