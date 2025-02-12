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

'''
sheep_counter = 110
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

blocks = int(input("Enter number of blocks you have: "))
block_needed_at_the_level = 0
height = 0
for counter in range(blocks):
        if block_needed_at_the_level+(height+1) <= blocks:
            height+=1
            block_needed_at_the_level += height
        else:
            break
print("Height:", height)
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
numbers = [10, 5, 7, 2, 1]
print("Original list contents:", numbers)  # Printing original list contents.
numbers[0] = 111
print("New list contents: ", numbers)  # Current list contents.










