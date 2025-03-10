from itertools import count

print("H")




















print("H")
print("e")
print("l")
print("l")
print("o")

print("Hello", "Suraj,", "how", "are", "you?")

'''
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
'''

#print("**********\n**********\n**********\n**********\n**********\n**********\n")

print("**********\n"*6 )

print("My", "name", "is", "Aditya", sep="_")
print("My", "name", "is", "Aditya", end="_")

print(2.2)
print(2)
print("2.2")
print(True)

print("Hello world")
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

blocks = int(input("Enter number of blocks:"))
height = 0
print("Blocks: ", blocks)
for counter in range(1, blocks+1):
    if blocks>= counter:
        blocks -= counter
        height += 1
    else:
        break
print("Height of pyramid is: ", height )