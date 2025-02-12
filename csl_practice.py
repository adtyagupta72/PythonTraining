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

number = int(input("Please enter a number, 0 to exit: "))
even = 0
odd = 0
while number !=0:
    if number % 2 == 0:
        even += 1
    else:
        odd += 1
    number = int(input("Please enter a number, 0 to exit: "))
print("Even numbers entered: ", even)
print("Odd numbers entered: ", odd)
