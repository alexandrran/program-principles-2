# Exercise 1
import re
p = re.compile('^a(b*)$')
m = p.search('abbb')
print(m.group())

# Exercise 2
import re
p = re.compile('^a(b{2,3}$)')
m = p.search('abbb')
print(m.group())

# Exercise 3
import re
p = re.compile('^[a-z]+_[a-z]+$')
m = p.search('abb_bca')
print(m.group())

# Exercise 4
import re
p = re.compile('^[A-Z][a-z]+$')
m = p.search('Python')
print(m.group())

# Exercise 5
import re
p = re.compile('^a.*?b$')
m = p.search('aergsdfsb')
print(m.group())

# Exercise 6
import re


def replace_with_colon(a):
    modified_text = re.sub('[ ,.]', ':', text)
    return modified_text


text = "Test tut tat kat cut."
result = replace_with_colon(text)
print(result)

# Exercise 7
def snake_to_camel(word):
    return ''.join(x.capitalize() or '_' for x in word.split('_'))


print(snake_to_camel('python_exercises'))

# Exercise 8
import re

def split_at_uppercase(text):
    return re.findall('[A-Z][^A-Z]*', text)

string = "TheLongAndWindingRoad"
result = split_at_uppercase(string)
print(result)

# Exercise 9
import re

def capital_words_spaces(str1):
    return re.sub(r"(\w)([A-Z])", r"\1 \2", str1)

print(capital_words_spaces("PythonIsHard"))

# Exercise 10
import re

def camel_to_snake(camel_string):
    snake_string = re.sub(r'(?<!^)(?=[A-Z])', '_', camel_string).lower()
    return snake_string


print(camel_to_snake("PythonExercises"))


