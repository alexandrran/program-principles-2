# Exercise 1
def convertation(grams):
    print(grams * 28.3495231)


grams = int(input("Enter the number of grams: "))
convertation(grams)

# Exercise 2
def convertation(F):
    C = int((5 / 9) * (F - 32))
    print(C)


temperature = int(input("Enter the temperature in Fahrenheit: "))
convertation(temperature)

# Exercise 3
def solve(numheads, numlegs):
    chickenlegs = numheads * 2
    rabbitlegs = (numlegs - chickenlegs)
    rabbits = rabbitlegs // 2
    chickens = numheads - rabbits
    if rabbits and chickens >= 0:
        print("Rabbits: ", rabbits)
        print("Chickens: ", chickens)
    else:
        print("Incorrect inputs")


heads = int(input("Enter number of heads: "))
legs = int(input("Enter number of legs: "))
solve(heads, legs)

# Exercise 4
def filter_prime(primes):
    for i in primes:
        is_prime = True
        if i < 2:
            is_prime = False
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
        if is_prime:
            print(i)


my_list = [1,2,3,4,5,6,7,8,9,10]
filter_prime(my_list)

# Exercise 5
def tostring(List):
    return ''.join(List)


def permute(a, l, r):
    if l == r:
        print(tostring(a))
    else:
        for i in range(l, r):
            a[l], a[i] = a[i], a[l]
            permute(a, l + 1, r)
            a[l], a[i] = a[i], a[l]  # backtrack


string = "hello"
n = len(string)
a = list(string)
permute(a, 0, n)

# Exercise 6
def reverse_string(str):
    words = str.split()
    reversed_words = ' '.join(reversed(words))
    print(reversed_words)


sentence = input("Enter a sentence: ")
reverse_string(sentence)

# Exercise 7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False


print(has_33([1, 3, 1, 3]))
print(has_33([1, 3, 3]))
print(has_33([3, 1, 3]))

# Exercise 8
def spy_game(a):
    if len(a) < 3:
        return False
    else:
        for i in range(len(a)):
            if a[i] == 0:
                for j in range(i+1, len(a)):
                    if a[j] == 0:
                        for k in range(j+1, len(a)):
                            if a[k] == 7:
                                return True
    return False


print(spy_game([1, 2, 4, 0, 0, 7, 5]))
print(spy_game([1, 0, 2, 4, 0, 5, 7]))
print(spy_game([1, 7, 2, 0, 4, 5, 0]))

# Exercise 9
import math


def sphere_volume(radius):
    return 4/3 * math.pi * radius**3


print(sphere_volume(int(input("Enter radius: "))))

# Exercise 10
def unique_elements(input_list):
    new_list = []
    for item in input_list:
        if item not in new_list:
            new_list.append(item)
    return new_list


my_list = [1, 2, 2, 3, 3, 4, 4, 5, 6, 6, 7, 7]
unique_result = unique_elements(my_list)
print("Unique elements:", unique_result)

# Exercise 11
def is_palindrome(word):
    word = word.lower()
    word = ''.join(c for c in word if c.isalnum())
    return word == word[::-1]


print(is_palindrome('madam'))

# Exercise 12
def histogram(numbers):
    for number in numbers:
        print(number * '*')


print(histogram([4, 9, 7]))

# Exercise 13
import random


def guess_the_number():
    number = random.randint(1, 20)
    name = input('Hello! What is your name? ')
    print(f'Well, {name}, I am thinking of a number between 1 and 20.')
    num_guesses = 0
    while True:
        guess = int(input('Take a guess. '))
        num_guesses += 1
        if guess < number:
            print('Your guess is too low.')
        elif guess > number:
            print('Your guess is too high.')
        else:
            print(f'Good job, {name}! You guessed my number in {num_guesses} guesses!')
            break


guess_the_number()
