class GreatestNumber:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def find_greatest(self):
        if self.num1 >= self.num2 and self.num1 >= self.num3:
            return "num1 is the greatest"
        elif self.num2 >= self.num1 and self.num2 >= self.num3:
            return "num2 is the greatest"
        else:
            return "num3 is the greatest"

# Taking input from user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

# Creating object
g = GreatestNumber(a, b, c)

# Calling method
print(g.find_greatest())
