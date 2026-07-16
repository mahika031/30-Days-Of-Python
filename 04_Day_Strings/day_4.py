
# Single line comment
letter = 'M'                # A string could be a single character or a bunch of texts
print(letter)               # M
print(len(letter))          # 1
greeting = 'Namaste!!!'  # String could be  a single or double quote,"Hello, World!"
print(greeting)             # Namaste!!!
print(len(greeting))        # 10
sentence = "Yes, I'm enjoying 30 days of python challenge"
print(sentence)
print()

# Multiline String
multiline_string = '''I am a student.
I'm currently on DAY 4 of this python learning challenge,
and I'm learning a lot'''
print(multiline_string)
# Another way of doing the same thing
multiline_string = """I am a student.
I'm currently on DAY 4 of this python learning challenge,
and I'm learning a lot."""
print(multiline_string)
print()

# String Concatenation
first_name = 'Mahika'
last_name = 'Singh'
space = ' '
full_name = first_name + space + last_name
print(full_name)  # Mahika Singh
# Checking length of a string using len() builtin function
print(len(first_name))  # 6
print(len(last_name))   # 5
print(len(first_name) > len(last_name))  # True
print(len(full_name))  # 12
print()

# Unpacking characters
language = 'Python'
a, b, c, d, e, f = language  # unpacking sequence characters into variables
print(a)  # P
print(b)  # y
print(c)  # t
print(d)  # h
print(e)  # o
print(f)  # n
print()

# Accessing characters in strings by index
language = 'Python'
first_letter = language[0]
print(first_letter)  # P - The first letter has 0 as its index
second_letter = language[1]
print(second_letter)  # y 
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter)  # n - The last index here would be 5

# If we want to start from right end we can use negative indexing. -1 is the last index
language = 'Python'
last_letter = language[-1]
print(last_letter)  # n - The last letter index would start from -1
second_last = language[-2]
print(second_last)  # o
print()

# Slicing
language = 'Python'
# starts at zero index and up to 3 but not include 3
first_three = language[0:3] #Pyt - Index 0,1,2 are printed
print(first_three)
last_three = language[3:6]
print(last_three)  # hon - Index 3,4,5 are printed
# Another way
last_three = language[-3:]
print(last_three)   # hon
last_three = language[3:]
print(last_three)   # hon

# Skipping character while splitting Python strings
language = 'Python'
pto = language[0:6:2]
print(pto)  # Pto - Index 0,2,4
print()

# Escape sequence
print('I hope every one enjoying the python challenge.\nDo you ?')  # line break
print('Days\tTopics\tExercises') #\t - Adds some space
print('Day 1\t3\t5')
print('Day 2\t3\t5')
print('Day 3\t3\t5')
print('Day 4\t3\t5')
print('This is a back slash  symbol (\\)')  # To write a back slash
print('In every programming language it starts with \"Hello, World!\"')
print()

# String Methods
# capitalize(): Converts the first character the string to Capital Letter
challenge = 'thirty days of python'
print(challenge.capitalize())  # 'Thirty days of python'
print()

# count(): returns occurrences of substring in string, count(substring, start=.., end=..)
challenge = 'thirty days of python'
print(challenge.count('y'))  # 3 - 'y' has appeared 3 times in the string
print(challenge.count('y', 7, 14))  # 1 - between index 7 and 13 'y' has appeared 1 time
print(challenge.count('th'))  # 2`
print()

# endswith(): Checks if a string ends with a specified ending
challenge = 'thirty days of python'
print(challenge.endswith('on'))   # True
print(challenge.endswith('tion'))  # False
print()

# expandtabs(): Replaces tab character with spaces, default tab size is 8. It takes tab size argument
challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())   # 'thirty  days    of      python'
print(challenge.expandtabs(10))  # 'thirty    days      of        python'
print()

# find(): Returns the index of first occurrence of substring
challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th'))  # 0
print()

# format()	formats string into nicer output
first_name = 'Mahika'
last_name = 'Singh'
job = 'student'
country = 'India'
sentence = 'I am {} {}. I am a {}. I live in {}.'.format(
    first_name, last_name, job, country)
print(sentence)  # I am Mahika Singh. I am a student. I live in India.

radius = 10
pi = 3.14
area = pi  # radius ## 2
result = 'The area of circle with {} is {}'.format(str(radius), str(area))
print(result)  # The area of circle with 10 is 314.0
print()

# index(): Returns the index of substring
challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th'))  # 0
print()

# isalnum(): Checks alphanumeric character
challenge = 'ThirtyDaysPython'
print(challenge.isalnum())  # True

challenge = '30DaysPython'
print(challenge.isalnum())  # True

challenge = 'thirty days of python'
print(challenge.isalnum())  # False

challenge = 'thirty days of python 2019'
print(challenge.isalnum())  # False
print()

# isalpha(): Checks if all characters are alphabets
challenge = 'thirty days of python'
print(challenge.isalpha())  # True
num = '123'
print(num.isalpha())      # False
print()

# find(): returns the index of the first occurrence of a character or substring in a string
challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th'))  # 0
print()

# isdigit(): Checks Digit Characters
challenge = 'Thirty'
print(challenge.isdigit())  # False
challenge = '30'
print(challenge.isdigit())   # True
print()

# isdecimal():Checks decimal characters
num = '10'
print(num.isdecimal())  # True
num = '10.5'
print(num.isdecimal())  # False
print()

# isidentifier():Checks for valid identifier means it check if a string is a valid variable name
challenge = '30DaysOfPython'
print(challenge.isidentifier())  # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier())  # True
print()

# islower():Checks if all alphabets in a string are lowercase
challenge = 'thirty days of python'
print(challenge.islower())  # True
challenge = 'Thirty days of python'
print(challenge.islower())  # False
print()

# isupper(): returns if all characters are uppercase characters
challenge = 'thirty days of python'
print(challenge.isupper())  # False
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper())  # True
print()

# isnumeric():Checks numeric characters
num = '20'
print(num.isnumeric())      # True
print('ten'.isnumeric())    # False
print()

# join(): Returns a concatenated string
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '#, '.join(web_tech)
print(result)  # 'HTML# CSS# JavaScript# React'
print()

# strip(): Removes both leading and trailing characters
challenge = ' thirty days of python '
print(challenge.strip('y'))  # 5
print()

# replace(): Replaces substring inside
challenge = 'thirty days of python'
print(challenge.replace('python', 'coding'))  # 'thirty days of coding'
print()

# split():Splits String from Left
challenge = 'thirty days of python'
print(challenge.split())  # ['thirty', 'days', 'of', 'python']
print()

# title(): Returns a Title Cased String
challenge = 'thirty days of python'
print(challenge.title())  # Thirty Days Of Python
print()

# swapcase(): Checks if String Starts with the Specified String
challenge = 'thirty days of python'
print(challenge.swapcase())   # THIRTY DAYS OF PYTHON
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON
print()

# startswith(): Checks if String Starts with the Specified String
challenge = 'thirty days of python'
print(challenge.startswith('thirty'))  # True
challenge = '30 days of python'
print(challenge.startswith('thirty'))  # False
print()

#OUTPUT =>
'''
M
1
Namaste!!!
10
Yes, I'm enjoying 30 days of python challenge

I am a student.
I'm currently on DAY 4 of this python learning challenge,
and I'm learning a lot
I am a student.
I'm currently on DAY 4 of this python learning challenge,
and I'm learning a lot.

Mahika Singh
6
5
True
12

P
y
t
h
o
n

P
y
n
n
o

Pyt
hon
hon
hon
Pto

I hope every one enjoying the python challenge.
Do you ?
Days    Topics  Exercises
Day 1   3       5
Day 2   3       5
Day 3   3       5
Day 4   3       5
This is a back slash  symbol (\)
In every programming language it starts with "Hello, World!"

Thirty days of python

3
1
2

True
False

thirty  days    of      python
thirty    days      of        python

5
0

I am Mahika Singh. I am a student. I live in India.
The area of circle with 10 is 3.14

5
0

True
True
False
False

False
False

5
0

False
True

True
False

False
True

True
False

False
True

True
False

HTML#, CSS#, JavaScript#, React

 thirty days of python 

thirty days of coding

['thirty', 'days', 'of', 'python']

Thirty Days Of Python

THIRTY DAYS OF PYTHON
tHIRTY dAYS oF pYTHON

True
False

'''