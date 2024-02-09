# Exercise 1
class StringInputOutput:
    def getString(self):
        return input("Enter a string: ")

    def printString(self, s):
        print(s.upper())


str = StringInputOutput()
input_string = str.getString()
str.printString(input_string)


# Exercise 2

class Shape:
    def __init__(self):
        pass

    def area(self):
        print("Area of the shape:", 0)


class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        a = self.length * self.length
        print(f"The area of a square with a side length of {self.length} is {a}")


s = Square(2)
s.area()

# Exercise 3
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


rectangle = Rectangle(4, 6)
print(f"Area of the rectangle: {rectangle.area()}")


# Exercise 4
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point coordinates: ({self.x}, {self.y})")

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def dist(self, other_point):
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        return math.sqrt(dx**2 + dy**2)


point1 = Point(3, 4)
point2 = Point(7, 9)

point1.show()
point2.show()

distance = point1.dist(point2)
print(f"Distance between the points: {distance:.2f} units")

# Exercise 5


class Account:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdraw ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")


account1 = Account(owner="Alexandr", initial_balance=1000)
account1.deposit(500)
account1.withdraw(200)
account1.withdraw(1500)


# Exercise 6
import math


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def filter_primes(numbers):
    return list(filter(lambda x: is_prime(x), numbers))


# Example usage:
my_numbers = [10, 21, 3, 8, 9, 11, 44, 62, 100, 19]
prime_numbers = filter_primes(my_numbers)
print("Prime numbers in the list:", prime_numbers)
