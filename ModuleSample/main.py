import mod1

my_list = [i + 1 for i in range(5)]
print("Calling module's function: ", mod1.suml(my_list))
print("Calling module's function: ", mod1.prodl(my_list))
print(mod1.suml(my_list) == 15)
print(mod1.prodl(my_list) == 120)