from itertools import count
'''
print("H")




















print("H")
print("e")
print("l")
print("l")
print("o")

print("Hello", "Suraj,", "how", "are", "you?")


Hello


H
e
l
l
o
'''

'''
**********
**********
**********
**********
**********
**********


#print("**********\n**********\n**********\n**********\n**********\n**********\n")

print("**********\n"*6 )

print("My", "name", "is", "Aditya", sep="_")
print("My", "name", "is", "Aditya", end="_")

print(2.2)
print(2)
print("2.2")
print(True)

print("Hello world")

a = 10
b = "Aditya"
c = "Software Developer"

#   a = myFunction()
#   Use of a => storing age
#   Use of b => store name

age = 10
name = "Aditya"

name = input("Enter your name: ")
print("Your name is :", name)

print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")



while True:
    print("I am stuck In a loop")'''

'''
1. declare variables even and odd with vlue 0 to count number of evens and odds
2. read a number
3. start a loop which ends on number being 0
4. Check if the number entered is even or odd
5. Increment the even or odd number count
6. read number input
7. after the loop, print even count and odd count
'''

# number = int(input("Please enter a number, 0 to exit: "))
# even = 0
# odd = 0
# while number !=0:
#     if number % 2 == 0:
#         even += 1
#     else:
#         odd += 1
#     number = int(input("Please enter a number, 0 to exit: "))
# print("Even numbers entered: ", even)
# print("Odd numbers entered: ", odd)

# counter = 0
# while counter < 100:
#     counter += 1
#     print("Counter: ", counter)

# for counter in range(100):
#     pass
# print("Counter: ", counter+1)

# for counter in range(2, 8):
#     print("The value of counter is currently: ", counter)

# for counter in range(2, 8, 3):
#     print("The value of counter is currently", counter)
# print("Going in For loop:")
# for counter in range(1, 1):
#     print("The value of counter is currently", counter)
# print("Out of For loop!")
# print("Going in For loop:")
# for counter in range(2, 1):
#     print("The value of counter is currently", counter)
# print("Out of For loop!")

# power = 1
# for expo in range(16):
#     print("2 to the power of", expo, "is", power)
#     power *= 3

# 2 to the power of 0 is 1
# 2 to the power of 1 is 2
# 2 to the power of 2 is 4

# for counter in range(1, 11):
#     print("2 * ", counter, "=", counter*2)

# import time
# for counter in range(5):
#     if counter == 2:
#         # go out
#         continue
#     print(counter+1, "Mississippi")
#     time.sleep(1)
#
# print("Read or not, here I come!")


# word = input("Please enter a word: ")
# print("Word is: ", word)
# word = word.upper()
# word_without_vowels = ""
# for itr in word:        # word = ADITYA     itr = A
#     print("Letter is: ", itr)
#     if itr == "A" or itr == "E" or itr == "I" or itr == "O" or itr == "U":
#         continue
#     word_without_vowels += itr
# print("Non eaten words are: ", word_without_vowels)

# counter = 5
# while counter < 5:
#     print("Counter: ", counter)
#     counter += 1
# else:
#     print("else counter: ", counter)

# for counter in range(5):
#     print(counter)
# else:
#     print("else:", counter)
# counter = 111
# for counter in range(2, 1):
#     print(counter)
# else:
#     print("else:", counter)

# blocks = int(input("Enter number of blocks:"))
# height = 0
# print("Blocks: ", blocks)
# for counter in range(1, blocks+1):
#     if blocks>= counter:
#         blocks -= counter
#         height += 1
#     else:
#         break
# print("Height of pyramid is: ", height )

# c0 = int(input("Enter the value of c0:"))
# if c0 <= 0:
#     print("c0 cannot be zero and less then zero")
# else:
#     counter = 0
#     while c0!= 1:
#         if c0 % 2 ==0:
#             c0 /= 2
#         else:
#             c0 = 3*c0 +1
#         print("c0: ", c0)
#         counter += 1
#     print("Final c0: ", c0, "\n steps it took:", counter)

# numbers = [10, 5, 7, 2, 1]
# print("List contents: ", numbers)  # Current list contents

# print("first element content: ", numbers[0])  # Current list contents.
# print("second element content: ", numbers[1])  # Current list contents.
# print("third element content: ", numbers[2])  # Current list contents.
# print("fourth element content: ", numbers[3])  # Current list contents.
# print("fifth element content: ", numbers[4])  # Current list contents.

# numbers[0] = 111
# print("New list contents: ", numbers)  # Current list contents.

# numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
# print("New list contents:", numbers)  # Printing current list contents.

# print(len(numbers))

# del numbers[1]
# print(len(numbers))
# print(numbers)

# numbers = [111, 7, 2, 1]
# print(numbers[-1])

# numbers = [111, 7, 2, 1]
# print(numbers[-2])


# number = [1, 2, 3, 4, 5]
# var = int(input("Enter a number:"))
# # print(len(number)//2)
# number[ len(number)//2 ] = var
# print(number)

# list = [5, 4, 3, 2, 1]
# print("Current List", list)
# list.append(6)
# print("Updated list after append:", list)

# list.insert(2, 7)
# print("Updated list after insert:", list)
# list.insert(0, 8)
# print("Updated list after insert:", list)

# list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#
# for count in range(len(list)):
#     print(list[count])
#
# list=[]
# for count in range(10):
#     list.append(count+1)
# print(list)

# list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# for count in range(10):
#     list[count] +=1
# print(list)
#
# list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# sum = 0
# for count in range(len(list)):
#     sum = sum + list[count]
# print(sum)

'''
count   0   0   1   2   3       4       5       6       7       8       9
sum     0   10  30  60  100     150     210     280     360     450     550
'''

# numbers = [10, 5, 7, 2, 1]
# print("0th Element: ", numbers[0])
# print("1th Element: ", numbers[1])
# print("2th Element: ", numbers[2])
# print("3th Element: ", numbers[3])
# print("4th Element: ", numbers[4])
#
# count = 0
# print("0th Element: ", numbers[count])
# count+=1
# print("1th Element: ", numbers[count])
# count+=1
# print("2th Element: ", numbers[count])
# count+=1
# print("3th Element: ", numbers[count])
# count+=1
# print("4th Element: ", numbers[count])
#
# numbers = [1, 2, 3, 4, 5]
# num = int(input("Please enter an integer value:"))
# numbers[len(numbers) // 2] = num
# print(numbers)


# list = [10, 1, 8, 3, 5]
#        0  1  2  3  4
#traversing a list

# for count in range(len(list)):
#     # print("Index: ", count)
#     # print("Element: ", list[count])
#     print("list[", count,"] => ", list[count])
#
# for element in list:
#     print("element => ", element)

#swapping list elements
# print(list)
# list[0], list[4] = list[4], list[0]
# list[1], list[3] = list[3], list[1]
# print(list)

# list = [9, 1, 3, 4, 7, 8, 6, 5, 2]
# count = 0
# for i in range(len(list)-1):
#     for j in range(len(list)-1-i):
#         if list[j] > list[j+1]:
#             list[j], list[j + 1] = list[j+1], list[j]
#         count += 1
#
# print(list)
# print("Loop ram for :",count," times")

#list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print("list before reverse = ",list)
# print("Debugging: len(list) // 2 =", len(list) // 2)
#
# if len(list) // 2 %2 == 0:
#     t = len(list) / 2
# else:
#     t = len(list) // 2 - 1
# print("Debugging: type(t): ", type(t))
# t = int(t)
# print("Debugging: type(t): ", type(t))
# for index in range(t):
#     list[index], list[-(index + 1)] = list[-(index+1)], list[index]
# print("list after reverse = ",list)

# number = [11, 3, 15, 5, 1, 9, 7, 17, 13]
# max = -1
# for element in number:
#     if max < element:
#         max = element
# print("Max value is: ", max)
# found = 0
# for index in range(len(number)):
#     if number[index] == 5:
#         print("Found 5 at index:", index)
#         found = 1
#         break
#
# if found == 0:
#     print("Sorry, 5 is not found!")

# lottery = [3, 7, 11, 42, 34, 49]
# drawn = [5, 11, 9, 42, 3, 49]
# hit = 0
# for element in lottery:
#     if element in drawn:
#        hit +=1
# print(hit)

# list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
# deleted = []
# for index in range(len(list)-1):
#     for index1 in range(index + 1, len(list)):
#         if index1 not in deleted:
#             if list[index] == list[index1]:
#                 deleted.append(index1)
# print(list)
# print(deleted)
# deleted.sort()
# print(deleted)
# for index in range(len(deleted)):
#     del list[deleted[len(deleted)-(index+1)]]
# print(list)

# def message(number):
#     print("Enter a number:", number)
# #message(10)
# number = 1234
# message(1)
# print("number:", number)

# def introduction(first_name, last_name):
#     print("Hello, my name is", first_name, last_name)
#
# introduction(first_name = "James", last_name = "Bond")
# introduction(last_name = "Skywalker", first_name = "Luke")
#
# def testFunction():
#     print("Function execution")
#     #return
#
# var = testFunction()
# print("var:", var)

# def is_year_leap(year):
#     if year % 4 == 0 and year % 100 != 0:
#         return True
#     elif year % 400 == 0:
#         return True
#     else:
#         return False
#
# test_data = [1900, 2000, 2016, 1987]
# test_results = [False, True, True, False]
# for i in range(len(test_data)):
#     yr = test_data[i]
#     print(yr,"->",end="")
#     result = is_year_leap(yr)
#     # print("result: ", result)
#     if result == test_results[i]:
#         print("OK")
#     else:
#         print("Failed")

# def fac(n):
#     if n<=1:
#         print("n = ", n)
#         print("returning 1 from less than equals to 1")
#         return 1
#     else:
#         print("calling fac(",n-1,") ")
#         res = fac(n - 1) * n
#         print("finally returning res=", res)
#         return res
#
# print(fac(5))

# def fib(n):
#     if n < 1:
#         return None
#     if n < 3:
#         return 1
#     res = fib(n - 1) + fib(n - 2)
#     print(res)
#     return res
# print(fib(10))

# tuple_1 = (1,2, 3, 4, 5)
# tuple_2 = 1, 2, 3, 4, 5
# print(tuple_1)
# print(tuple_2)
# print(type(tuple_1))
# print(type(tuple_2))
#
# empty_tuple = ()
# print(empty_tuple)
# print(type(empty_tuple))
#
# new_tuple = 1,
# print(new_tuple)
# print(type(new_tuple))
#
# list = [1, 2, 3, 4, 5]
# list2 = [6, 7, 8, 9, 10]
#
# list3 = list+list2
# print(list3)
# list4 = list*3
# print(list4)

# tuple_1 = (1,2, 3, 4, 5)
# tuple_2 = 6, 7, 8, 9, 10
# tuple_3 = tuple_1 + tuple_2
# print(tuple_3)
# tuple_4 = tuple_3 *2
# print(tuple_4)
#
# for element in tuple_1:
#     print(element)

# dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
# print(dictionary)
# dictionary.update({"adam":"adaam"})
# print(dictionary)
# dictionary.update({"zadam":"zadaam"})
# print(dictionary)
# #dictionary.sort()
# for key in dictionary:
#     print(key,"->",dictionary[key])
#
# dictionary.popitem()
# print(dictionary)
# dictionary.popitem()
# print(dictionary)
# dictionary.popitem()
# print(dictionary)
# dictionary["adam"] = 123
# print(dictionary)
# dictionary.popitem()
# print(dictionary)
#
# dictionary.clear()
# print(dictionary)

# copy_dictionary = dictionary.copy()
# print(copy_dictionary)
# copy_dictionary["cat"] = "No chat"
# print(copy_dictionary)
# print(dictionary)
# for key in dictionary.keys():
#     print(key, "->", dictionary[key])

# for key, value in dictionary.items():
#     print(key, "->", value)
#
# phone_numbers = {'boss' : 5551234567, 'Suzy' : 22657854310}
# empty_dictionary = {}
# print(dictionary)
# print(type(dictionary))
# print(phone_numbers)
# print(type(phone_numbers))
#
# print(dictionary['cat'])
# print(phone_numbers['Suzy'])

# list = [1,2 ,3, 4, 5]
# del list[:]     # []
# del list        #error
# school_class = {}
# while True:
#     name = input("Enter the student's name: ")
#     if name == '':
#         break
#
#     score = int(input("Enter the student's score (0-10): "))
#     if score not in range(0, 11):
#         break
#
#     if name in school_class:
#         school_class[name] += (score,)
#     else:
#         school_class[name] = (score,)
#
# for name in sorted(school_class.keys()):
#     adding = 0
#     counter = 0
#     for score in school_class[name]:
#         adding += score
#         counter += 1
#     print(name, ":", adding / counter)

# try:
#     value = int(input("Enter a value for reciprocal result:"))
#     print("The reciprocal of ", value, "is", 1 / value)
# except:
#     print("Sorry, my program is not working!")

# try:
#     value = int(input("Enter a value for reciprocal result:"))
#     try:
#         print("The reciprocal of ", value, "is", 1 / value)
#     except:
#         print("Please enter anything other then zero!")
# except:
#     print("Please enter something!, Blank is not acceptable!")

# try:
#     value = int(input("Enter a value for reciprocal result:"))
#     print("The reciprocal of ", value, "is", 1 / value)
# except ValueError:
#     print("Value entered is not appropriate!")
# except ZeroDivisionError:
#     print("Zero cannot be accepted as an input!")
# except:
#     print("Sorry for the inconvenience my code failed!")

# temperature = float(input('Enter current temperature:'))
# if temperature > 0:
#     print("Above zero")
# elif temperature < 0:
#     prin("Below zero")
# else:
#     print("Zero")

# import math
# print(math.exp(12))
#
# import mint     # make_money()
# print(mint.make_money())
#
# print(math.sin(1))

# def sin(x):
#     if 2 * x == pi:
#         return 0.99999999
#     else:
#         return None
#
# pi = 3.14
#
# print(sin(pi/2))
# print(math.sin(math.pi/2))

# from math import sin, pi, exp
# # Selective import form module
#
# print(sin(pi/2))
# print(exp(2))

# import math as ganit #aliasing
# print(ganit.sin(ganit.pi/2))
# print(ganit.exp(2))

# from math import sin as si, exp as e, pi as p
# print(si(p/2))
# print(e(2))

# import math
# print(math.sin(math.pi/2))
# print(dir(math))
# print("asinh" in dir(math))
# from math import pi, radians, degrees, sin, cos, tan, asin
# ad = 90
# ar = radians(ad)
# ad = degrees(ar)
#
# print(ad == 90.)
# print(ar == pi / 2.)
# print(sin(ar) / cos(ar) == tan(ar))
# print(asin(sin(ar)) == ar)

# from random import random, seed, randrange, randint, choice, sample
# #seed()
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in range(5):
#     print(choice(my_list))
#     print(sample(my_list, 4))
#     print(sample(my_list, 7))
#     #print(random(), end=",")
    #print(randrange(1, 101, 5))
    #print(randint(1, 10))

# from platform import platform, machine, processor, system, version, python_implementation, python_version_tuple
#
# print(platform())
# print(platform(1))
# print(platform(0, 1))
# print("------------")
# print(platform())
# print(platform(True, False))
# print(platform(False, True))
# print(platform(True, True))
# print("------------")
# print(machine())
# print(processor())
# print(system())
# print(version())
# print(python_implementation())
# print(python_version_tuple())

# word = "Hello"
# print(len(word))
#
# word = ""
# print(len(word))
#
# word = " "
# print(len(word))
#
# word = "I\"m"
# print(len(word))
#
# word = '''whebckwebc
# 1
# 2
# 3
# 3
# wevkjnwejvkn'''
# print(len(word))
#
# word = "Aditya\nGupta"
# print(len(word))
# print(word)
#
# stringOne = "One"
# stringTwo = "Two"
#
# print(stringOne+stringTwo)
# print(stringOne*4)
# print(4*stringTwo)
#
# print(ord("a"))
# print(ord(" "))
# #print(ord(""))
#
# print(chr(97))
# print(chr(98))
#
# print(chr(ord("a")))
#
# word = "My string is awesome!"
# print(word[5])
# print(word[14])
#
# for index in range(len(word)):
#     if word[index] == "a" or \
#             word[index] == "e" or \
#             word[index] == "i" or \
#             word[index] == "o" or\
#             word[index] == "u":
#         print("1", end="")
#     else:
#         print(word[index], end="")
# print(word)
#
# for char in word:
#     print("char: ",char)

alpha = "abdefg"
print(alpha[1:3])
print(alpha[3:])
print(alpha[3:-2])
print(alpha[-3:4])
print("-> ", alpha[1:4:2])#
print(alpha[::2]) # range(start, end, step)
print(alpha[1::2])

alphabet = "abcdefghijklmnopqrstuvwxyz"

print("f" in alphabet)
print("f" not in alphabet)
print("fab" in alphabet)
