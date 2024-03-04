# # Exercise 1
my_list = [1, 2, 3, 4, 5]
print(eval("*".join(map(str, my_list))))


# Exercise 2
uppercase = 0
lowercase = 0
str = input("Input a string: ")
for i in str:
    if i.isupper():
        uppercase += 1
    elif i.islower():
        lowercase += 1
print(f'The number of upper case letters: {uppercase}, the number of lower case letters: {lowercase}')


# Exercise 3
str = input("Input a string: ")
str1 = str.lower()
if str1 == str1[::-1]:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")


# Exercise 4
import time
def delayed_sqrt(num, delay):
    time.sleep(delay / 1000)
    return num ** 0.5


number = int(input("Enter a number: "))
delay = int(input("Enter a delay: "))
print(f'The square root of {number} after {delay} miliseconds is {delayed_sqrt(number, delay)}')


# Exercise 5
def all_true(tuple):
    return all(tuple)


t = (True, True, True)
result = all_true(t)

print(result)

