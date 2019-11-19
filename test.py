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

name1 = input("Enter a name: ")
num2 = input("Enter an age: ")
print('Hello ' + name1 + ' i see that you are ' + num2 + ' years old!')

