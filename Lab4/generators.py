# Exercise 1
def gensquares(N):
    for i in range(N):
        yield i ** 2


n = int(input("Enter a number: "))
gen = gensquares(n)
for i in gen:
    print(i)


# Exercise 2
def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i
        else:
            continue


N = int(input("Input a number: "))
even_gen = list(even_numbers(N))
print(*even_gen, sep=", ")



# Exercise 3
def divisible_3_4_numbers(n):
    for i in range(n):
        if i % 3 == 0 or i % 4 == 0:
            yield i
        else:
            continue


N = int(input("Input a number: "))
divisible_gen = divisible_3_4_numbers(N)
for i in divisible_gen:
    print(i)


# Exercise 4
def squares(a, b):
    for num in range(a, b + 1):
        yield num ** 2


a = int(input("Enter a first number: "))
b = int(input("Enter a second number: "))
squares_gen = squares(a, b)
for square in squares_gen:
    print(square)


# Exercise 5
def gen_numbers(n):
    for i in range(n, -1, -1):
        yield i


N = int(input('Enter a number: '))
numbers_gen = gen_numbers(N)
for number in numbers_gen:
    print(number)

