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


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
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

print(list)
for count in range(len(list)):
    #print("count:", count) # 0 1 2 3 4 5 6 7 8 9
    print("list[-",count+1,"]:", list[-1*(count+1)])

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


list=[]

# for i in range(8):
#     list.append("WHITE_PAWN")

list = ["WHITE_PAWN" for i in range(8)]
# ["WHITE_PAWN","WHITE_PAWN","WHITE_PAWN","WHITE_PAWN","WHITE_PAWN",...."WHITE_PAWN"]
print(list)

squares = [x ** 2 for x in range(10)]
print(squares)

twos = [2 ** i for i in range(8)]
print(twos)

odds = [x for x in squares if x % 2 != 0 ]

print(odds)         #

board = []
for i in range(8):
    row = ["EMPTY" for j in range(8)]
    board.append(row)
    print(board[i])

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

temps = [[hour for hour in range(24)] for month in range(31)]
print(temps)
# Calculating Average noon temperature
sum=0
for day in range(31):
    sum=sum+temps[day][11]
avg=sum/31
print(avg)

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

def message():
    print("Enter a value: ")
print(message())    #
message = 1
# int
print(message)