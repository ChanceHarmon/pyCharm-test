from math import *  # should be at top of screen

#  Proof of Life

print('hello world')
# import pdb;pdb.set_trace()
user_name = 'Chance'
user_age = '34'
print('Hello, my name is ' + user_name + ' and I am ' + user_age + ' years old!')
user_name = 'Jaquelyn'
user_age = '36'
print('Hello, my name is ' + user_name + ' and I am ' + user_age + ' years old!')

#  strings

print("Harmon\nAcademy")
print("Harmon\"Academy")
print("Harmon\Academy")

phrase = "Harmon Academy"
print(phrase)
print(phrase + " is legit.")
print(phrase.lower() + " is legit.")
print(phrase.upper() + " is legit.")
print(phrase.isupper())
print(phrase.upper().isupper())
print(phrase.islower())
print(phrase.lower().islower())
print(len(phrase))
print(phrase[0])
print(phrase[4])
# 0 index like JS
print(phrase.index("a"))
print(phrase.replace("Harmon", "Gladiator"))

#  Numbers

print(23)
print(-2.0456)
print(3 + 4)
print(3 * 4 + 5)
print(3 * (4 + 5))
print(10 % 3)
my_num = 5
print(my_num)
print(str(my_num))
print(str(my_num) + " my number")
print(abs(my_num))  # same as -5
print(pow(4, 2))
print(max(4, 8))
print(min(4, 8))
print(round(7.879))
print(floor(4.678))
print(ceil(4.678))
print(sqrt(16))

# num1 = input("Enter a number: ")
# num2 = input("Enter another number: ")
# result = int(num1) + int(num2)  # whole numbers
# result2 = float(num1) + float(num2)  # can use decimals
# print(result)
# print(result2)

# mad libs
# color = input("Enter a color: ")
# plural_noun = input("Enter a plural noun: ")
# celebrity = input("Enter a celebrity: ")

# print("Roses are " + color)
# print(plural_noun + " are blue")
# print("I love " + celebrity)

# lists/arrays

friends = ["Brad", "Yosh", "David", "Jim", "James"]
print(friends[1])
print(friends[-1])
print(friends[1:4])
friends[2] = "Josh"
print(friends[2])

lucky_numbers = [2, 4, 7, 8, 3]
# friends.extend(lucky_numbers)
friends.append("Rocky")
friends.insert(1, "Joe")  # two parameters, index and then the value
friends.remove("Josh")
# friends.clear() clears the list
# friends.pop() same as JS
print(friends.index("Brad"))
print(friends)
friends.sort()
print(friends)
lucky_numbers.reverse()
print(lucky_numbers)

# tuples data structure immutable, cant be changed or modified
# used for data that never changes
coordinates = (4, 5)

print(coordinates[0])


# functions
# keyword of def, def name():
# def say_hi():
#     print("Hello Chance")
#
# say_hi

# template literals (f"string {variable}")
def say_hi(name):
    print(f"Hello {name}")


say_hi("Chance")


def cube(num):
    return num*num*num


result = cube(4)

print(result)

# return breaks out of the function, no code after can be reached
# if statements

is_chance = True
is_happy = True
if is_chance:
    print('Chance is still at the keys')
else:
    print('Someone stole my computer!')

if is_chance or is_happy:
    print('Chance could be happy')

if is_chance and is_happy:
    print('Chance is happy!')
elif is_chance and not is_happy:
    print('Cheer up Chance')
else:
    print('Cheer up Stranger')


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(2, 4, 6))


# New calculator
#
# num1 = float(input('Enter the first number: '))
# operator = input('Enter the operation: ')
# num2 = float(input('Enter the second number: '))
#
# if operator == '+':
#     print(num1 + num2)
# elif operator == '-':
#     print(num1 - num2)
# elif operator == '/':
#     print(num1 / num2)
# elif operator == '*':
#     print(num1 * num2)
# else:
#     print('Invalid operator')


# Dictionaries
# check monthConversions?
month_conversions = {
    'Jan': 'January',
    'Feb': 'February',
    'Mar': 'March',
    'Apr': 'April',
    'May': 'May',
    'Jun': 'June',
    'Jul': 'July',
    'Aug': 'August',
    'Sep': 'September',
    'Oct': 'October',
    'Nov': 'November',
    'Dec': 'December'
}

print(month_conversions['Feb'])
print(month_conversions.get('Feb'))
print(month_conversions.get('Sas', 'Default text I added'))


# While loops




