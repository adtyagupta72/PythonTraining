# print("Hello world")
'''
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

'''
# sheep_counter = 110
# if sheep_counter >=120:
#     print("make_a_bed")
#     print("take_a_shower")
#     print("sleep_and_dream")
# print("feed the sheeps")

# weather_is_good = True
# if sheep_counter >=120:
#     if weather_is_good:
#         print("make_a_bed")
#         print("take_a_shower")
#         print("sleep_and_dream")
#     else:
#         if sheep_counter>200:
#             print("I cannot go out")
# else:
#     print("Not able to count sheep")
#
# print("feed the sheep")

# while True:
#     print("I'm stuck inside a loop.")

# for counter in range(10):
#     print("The value of counter is currently", counter)

# blocks = int(input("Enter number of blocks you have: "))
# block_needed_at_the_level = 0
# height = 0
# for counter in range(blocks):
#         if block_needed_at_the_level+(height+1) <= blocks:
#             height+=1
#             block_needed_at_the_level += height
#         else:
#             break
# print("Height:", height)
'''
blocks      7  
sum         0   0   1   3   6
counter         0   1   2   3
height      0   1   2   3   4

Result:
block_size                  20
blocks_needed_at_level          1   3   6   10  15  21
height                          1   2   3   4   5   6
counter                         0   1   2   3   4   5

block_size      20
blocks_needed_at_level      0   1   3   6   10  15
height                      0   1   2   3   4   5   
counter                         0   1   2   3   4   5

Process
    for loop
        if block_needed_at_the_level+(height+1) <=block:
            height++
            block_needed_at_the_level += height
        else:
            breaks
        
'''
# numbers = [10, 5, 7, 2, 1]
# print("Original list contents:", numbers)  # Printing original list contents.
# numbers[0] = 111
# print("New list contents: ", numbers)  # Current list contents.


#list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# print("My List: ", list)
# print("5th element: ", list[4])
# del list[0]
# print("My List: ", list)
# print("5th element: ", list[4])
#
# del list[4]
# print("My List: ", list)
# print("5th element: ", list[4])
#
# for count in range(len(list)-1):
#     del list[0]
#     print(list)
# print("My List: ", list)
#
# del list
# print("My List: ", list)

# print(list)
# for count in range(len(list)):
#     #print("count:", count) # 0 1 2 3 4 5 6 7 8 9
#     print("list[-",count+1,"]:", list[-1*(count+1)])

#print("list[-11]", list[-11])

# abc.print(list)
# abc is changed
#
# print(list)

# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# for element in list:                # oiterator is givinng element one-by-one
#     print("element: ", element)
#
# for index in range(len(list)):
#     print("index: ", index)
#     print("element: ", list[index])

# list = [8, 10, 6, 2, 4]
# counter = 0
# for count in range(len(list)):
#     for count1 in range(len(list)-1-count):
#         if list[count1+1] < list[count1]:
#             list[count1 + 1], list[count1] = list[count1], list[count1+1]
#         counter+=1
# print(list)
# print(counter)
'''
count       0        0       0       0       
count1      0        1       2       3     
check1    (8, 10)   (10,6)  (6,2)   (6,4)   => [8, 6, 2, 4, 10]     =>10    0
check2    (8,6)     (8,2)   (8,4)           => [6, 2, 4, 8, 10]     =>8     1
check3    (6, 2)    (6,4)                   => [2, 4, 6, 8, 10]                 2
check4    (2,4)                             => [2, 4, 6, 8, 10]
'''

# Slice operator
# list_1 = [1]
# list_2 = list_1[:]
# list_1[0] = 2
# print(list_2)
#
# my_list = [10, 8, 6, 4, 2]
# new_list = my_list[1:3]
# print(new_list)     #8, 6


# list=[]
#
# # for i in range(8):
# #     list.append("WHITE_PAWN")
#
# list = ["WHITE_PAWN" for i in range(8)]
# # ["WHITE_PAWN","WHITE_PAWN","WHITE_PAWN","WHITE_PAWN","WHITE_PAWN",...."WHITE_PAWN"]
# print(list)
#
# squares = [x ** 2 for x in range(10)]
# print(squares)
#
# twos = [2 ** i for i in range(8)]
# print(twos)
#
# odds = [x for x in squares if x % 2 != 0 ]
#
# print(odds)         #
#
# board = []
# for i in range(8):
#     row = ["EMPTY" for j in range(8)]
#     board.append(row)
#     print(board[i])

# [
#     ["EMPTY", "EMPTY", "EMPTY", "EMPTY", "EMPTY", "EMPTY", "EMPTY", "EMPTY"],
#     ["EMPTY", "EMPTY", "EMPTY", "EMPTY", "EMPTY", "EMPTY", "EMPTY", "EMPTY"],
#     ["EMPTY", "EMPTY", "EMPTY", "EMPTY", "EMPTY", "EMPTY", "EMPTY", "EMPTY"],
#     ["EMPTY", "EMPTY", "EMPTY", "EMPTY", "EMPTY", "EMPTY", "EMPTY", "EMPTY"],
#     ["EMPTY", "EMPTY", "EMPTY", "EMPTY", "EMPTY", "EMPTY", "EMPTY", "EMPTY"],
#     ["EMPTY", "EMPTY", "EMPTY", "EMPTY", "EMPTY", "EMPTY", "EMPTY", "EMPTY"],
#     ["EMPTY", "EMPTY", "EMPTY", "EMPTY", "EMPTY", "EMPTY", "EMPTY", "EMPTY"],
#     ["EMPTY", "EMPTY", "EMPTY", "EMPTY", "EMPTY", "EMPTY", "EMPTY", "EMPTY"],
# ]

# temps = [[hour for hour in range(24)] for month in range(31)]
# print(temps)
# Calculating Average noon temperature
# sum=0
# for day in range(31):
#     sum=sum+temps[day][11]
# avg=sum/31
# print(avg)

# Calculating highest temperature in the month
# highest=-200
# for day in range(31):
#     for hour in range(24):
#         highest = max(highest, temps[day][hour])
# print(highest)

# def message():
#     print("Hello")
#
# message = 1
# message()
# def hello(name): # defining a function
#     print("Hello,", name) # body of the function
#
# name = input("Enter your name: ")
# hello(name) # calling the function

# def message():
#     print("Enter a value: ")
# print(message())    #None
# message = 1
# # int
# print(message)

# def is_year_leap(year):
#     if (year % 4 == 0 and year % 100 != 0):
#         return True
#     if (year % 400 == 0):
#         return True
#     else:
#         return False
#
# def days_in_month(year, month):
#     if month == 2:
#         if is_year_leap(year):
#             return 29
#         else:
#             return 28
#     if month in (4, 6, 9, 11):
#         return 30
#     else:
#         return 31


# test_years = [1900, 2000, 2016, 1987]
# test_months = [2, 2, 1, 11]
# test_results = [28, 29, 31, 30]
# for i in range (len(test_years) ) :
#     yr = test_years [i]
#     mo = test_months [i]
#     print (yr, mo, "->", end="")
#     result = days_in_month (yr, mo)
#     if result == test_results[i] :
#         print ("OK")
#     else:
#         print ("Failed")

# def scope_test():
#     x = 148
#     print(x)
# scope_test()
# print(x)

# def scope_check():
#     print("Checking for scope of var: ", var)
#
# var = 1
# scope_check()
# print(var)

# var = 2
#
# def mult(x):
#     var = 5
#     return x * var
#
# print(mult(7))

# def scope_check():
# #    global var
#     var = 2        #Local
#     print("Checking for scope of var: ", var)
#
# global var
# #var = 1             #Global
# scope_check()
# print(var)

# def my_function(my_list_1):
#     print("Print #1:", my_list_1)
#     print("Print #2:", my_list_2)
#     my_list_1 = [0, 1]
#     print("Print #3:", my_list_1)
#     print("Print #4:", my_list_2)
#
#
# my_list_2 = [2, 3]
# my_function(my_list_2)
# print("Print #5:", my_list_2)

# tuple1 = (1, 2, 3, 4, 5)
# tuple2 = 1, 2, 3, 4, 5,
#
# print(tuple1)
# print(type(tuple1))
# print(tuple2)
# print(type(tuple2))
#
# tuple3 = ()
# print(tuple3)
# print(type(tuple3))
#
# tuple4 = 1,
# print(tuple4)
# print(type(tuple4))
#
# tuple5 = (1, 10, 100)
#
# tuple6 = tuple5+(1000, 10000)
# print(tuple6)
# print(type(tuple6))
#
# tuple7 = tuple6 * 3
# print(tuple7)
# print(type(tuple7))
# print(len(tuple7))
# print(10 in tuple7)
# print(20 not in tuple7)
# print(20 in tuple7)

# var = 123
#
# tuple = (1, 2, 3, var)
#
# print(tuple)
#
# t1 = (1,)
# t2 = (2,)
# t3 = (3, var)
#
# print(t1, t2, t3)
#
# t1, t2, t3 = t2, t3, t1
#
# print(t1, t2, t3)

dictionary = {
    "cat": "chat",
    "dog": "chien",
    "horse": "cheval"
}
# phone_numbers = {'boss': 5551234567, 'Suzy': 22657854310}
# empty_dictionary = {}
#
# print(dictionary)
# print(len(dictionary))
# print(phone_numbers)
# print(len(phone_numbers))
# print(empty_dictionary)
# print(len(empty_dictionary))
#
# print(dictionary['cat'])
# print(phone_numbers['Suzy'])
#print(phone_numbers['Suzy1'])

# for key in dictionary:
#     if key in dictionary:
#         print(key, "->", dictionary[key])
#     else:
#         print(key, "is not in dictionary")
#
# print(dictionary.keys())
# print(dictionary.keys())
# for key in dictionary.keys():
#     if key in dictionary:
#         print(key, "->", dictionary[key])
#     else:
#         print(key, "is not in dictionary")

# for animal, name in dictionary.items():
#     print("Animal:", animal, ", Name:", name)
#
# for name in dictionary.values():
#     print("Name:", name)
#
# newDictionary = dictionary # only reference was copied
#
# print("new Dictionary:", newDictionary)
# print("Dictionary:", dictionary)
#
# dictionary["cat"] = "abc"
#
# print("new Dictionary:", newDictionary)
# print("Dictionary:", dictionary)
#
# newDictionary = dictionary.copy()
#
# dictionary["dog"] = "def"
#
# print("new Dictionary:", newDictionary)
# print("Dictionary:", dictionary)
#
# # del dictionary["cat"]
# # print("Dictionary:", dictionary)
#
# newDictionary.update({"Parrot":"Jungle"})
# print("new Dictionary:", newDictionary)
# newDictionary.popitem()
# print("new Dictionary:", newDictionary)
#
# if "cat" in dictionary:
#     print("Cat is present")
#     print(dictionary["cat"])
# else:
#     print("Cat is not present!!")
#
# print(len(dictionary))
#
# dictionary.clear()
# print("Dictionary after clear", dictionary)
# del dictionary
# #print("Dictionary after del", dictionary)
#
# def collect_grades():
#     students = {}
#
#     while True:
#         name = input("Enter student name (blank to stop): ")
#         if name == "":
#             break
#
#         scores = ()
#         print("Enter scores:")
#         while True:
#             score_input = input("  Score (blank to finish): ")
#             if score_input == "":
#                 break
#
#             scores.append(float(score_input))
#
#             students[name] = scores
#
#     return students
#
# def calculate_averages(students):
#     averages = {}
#     for name in students:
#         total = sum(students[name])
#         count = len(students[name])
#         averages[name] = total / count
#     return averages
#
# def display_results(averages):
#     print("Average Scores:")
#     for name in (averages.keys()):
#         print({name},":", {averages[name]})
#
#
#
# student_data = collect_grades()
# averages = calculate_averages(student_data)
# display_results(averages)
# try:
#     value = int(input('Enter a natural number: '))
# except:
#     print("Valid input required")
#
#
# try:
#     print('The reciprocal of', value, 'is', 1 / value)
# except:
#     print("Value cannot be zero!")

# inputString = input('Enter a natural number: ')
#
# if inputString.isdigit():
#     value = int(inputString)
#     print('The reciprocal of', value, 'is', 1 / value)
#
# else:
#     print("you can't add String here....")


# try:
#     value = int(input('Enter a natural number: '))
#     print('The reciprocal of', value, 'is', 1 / value)
# #     1 - Input = 0
# #     2 - Input = character
# #     3 - Input = String
# except ValueError:
#     print("Value Invalid!")
# except ZeroDivisionError:
#     print("Value cannot be zero!")

# temperature = float(input('Enter current temperature:'))
# if temperature > 0:
#     print("Above zero")
# elif temperature < 0:
#     print("Below zero")
# else:
#     print("Zero")
#
# my_list = [x * x for x in range(5)]
#
#
# def fun(lst):
#     del lst[lst[2]]
#     return lst
#
#
# print(fun(my_list))

# x = 1
# y = 2
# x, y, z = x, x, y
# z, y, z = x, y, z
#
# print(x, y, z)
#
# lst = [i for i in range(-1, -2)]
#                     #start  end
# print(lst)
#
# tup = (1, 2, 4, 8)
# print(tup)
# tup = tup[-2:-1]
# print(tup)
# tup = tup[-1]
# print(tup)

#print(None + 1)
# a = 1
# print(None == a)
# print(None != a)
# def fun(x):
#     global y
#     y = x * x
#     return y
#
# fun(2)
# print(y)
#
# import math
# print("math.sin: ",math.sin)
# print("math.pi: ",math.pi)
# print(math.sin(math.pi/2))

# import math
#
# def sin(x):
#     if 2 * x == pi:
#         return 0.99999999
#     else:
#         return None
# pi = 3.14
#
# print(sin(pi/2))
# print(math.sin(math.pi/2))

# from math import sin, pi
# print(sin(pi/2))

# from math import sin, pi
# print(sin(pi / 2))
# pi = 3.14
# def sin(x):
#     if 2 * x == pi:
#         return 0.99999999
#     else:
#         return None
#
# print(sin(pi / 2))

# pi = 3.14
# def sin(x):
#     if 2 * x == pi:
#         return 0.99999999
#     else:
#         return None
#
# print(sin(pi / 2))
#
# from math import *
#
# print(sin(pi / 2))

# import math as m
# print("m.sin: ",m.sin)
# print("m.pi: ",m.pi)
# print(m.sin(m.pi/2))

# from math import pi as PI, sin as sine
# import math
# #print(sine(PI/2))
# print(dir(math))
# print("tan" in dir(math))
# if "tan" in dir(math):
#     print("Tan can be used from Math")

# from math import pi, radians, degrees, sin, cos, tan, asin
#
# ad = 90
# ar = radians(ad)
# ad = degrees(ar)
#
# print(ad == 90.)
# print(ar == pi / 2.)
# print(sin(ar) / cos(ar) == tan(ar))
# print(asin(sin(ar)) == ar)


# from math import ceil, floor, trunc
# x = 1.4
# y = 2.9
# print(floor(x), floor(y))
# print(floor(-x), floor(-y))
# print(ceil(x), ceil(y))
# print(ceil(-x), ceil(-y))
# print(trunc(x), trunc(y))
# print(trunc(-x), trunc(-y))
# from random import random
#
# for i in range(5):
#     print(random())

# import random
# # seed()
# #
# # for i in range(5):
# #     print(random())
# print(random.randrange(10), end=' ')
# print(random.randrange(0, 10), end=' ')
# print(random.randrange(0, 10, 1), end=' ')
# print(random.randint(0, 10))
#
# for i in range(10):
#     print(random.randint(1, 10), end=',')

from platform import platform, machine, processor, system, version

print(platform())
print(platform(1))
print(platform(0, 1))
print(platform(1, 1))

print(machine())
print(processor())
print(system())
print(version())

from platform import python_implementation, python_version_tuple
print(python_implementation())
pythonVersion = 0
for atr in python_version_tuple():
    print(atr)