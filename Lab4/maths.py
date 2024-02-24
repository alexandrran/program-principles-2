# Exercise 1
import math
print("Output radian: ", round(math.radians(int(input("Input degree:"))), 6))

# Exercise 2
h = int(input("Height: "))
a = int(input("Base, first value: "))
b = int(input("Base, second value: "))
print("Expected output: ", ((a + b) / 2) * h)

# Exercise 3
import math
n = int(input("Input number of sides: "))
a = int(input("Input the length of a side: "))
area = ((n * math.pow(a, 2)) / (4 * math.tan(math.pi / n)))
print(f"The area of the polygon is: {math.floor(area)} ")

# Exercise 4
a = int(input("Length of base: "))
h = int(input("Height of parallelogram: "))
area = a * h
print(f"Expected output: {float(area)}")
