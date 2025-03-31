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
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("list before reverse = ",list)
print("Debugging: len(list) // 2 =", len(list) // 2)

if len(list) // 2 %2 == 0:
    t = len(list) / 2
else:
    t = len(list) // 2 - 1
print("Debugging: type(t): ", type(t))
t = int(t)
print("Debugging: type(t): ", type(t))
for index in range(t):
    list[index], list[-(index + 1)] = list[-(index+1)], list[index]
print("list after reverse = ",list)












