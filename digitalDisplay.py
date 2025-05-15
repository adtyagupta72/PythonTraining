digitalDisplayList = [
'''
 ####
 #  #
 #  #
 #  #
 ####
''',
'''
    #
    #
    #
    #
    #
''',
'''
 ####
    #
 ####
 #  
 ####
''',
'''
 ####
    #
 ####
    #
 ####
''',
'''
 #  #
 #  #
 ####
    #
    #
''',
'''
 ####
 #  
 ####
    #
 ####
''',
'''
 ####
 #  
 ####
 #  #
 ####
''',
'''
 ####
    #
    #
    #
    #
''',
'''
 ####
 #  #
 ####
 #  #
 ####
''',
'''
 ####
 #  #
 ####
    #
 ####
''',
]
# check = True
# while check:
#     number = int(input("Please enter any number[-1 to exit]:"))
#     if number == -1:
#         check = False
#     print(digitalDisplayList[number])

check = True
while check:
    number = int(input("Please enter any number[-1 to exit]:"))
    if number == -1:
        check = False
    if number > 9:
        tempList = []
        tempNumber = number
        while tempNumber != 0:
            tempList.append(tempNumber%10)
            print(tempList)
            tempNumber = tempNumber/10
            print(tempNumber)
        for element in tempList:
            print(element)
    else:
        print(digitalDisplayList[number])