#import mod1
#from mod1 import suml, prodl

import sys, os.path
# my_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))+'/modules/')
# sys.path.append(my_dir)
# import  mo
sys.path.append('/Users/aditya/Documents/Explore/python/TemproryRepo/ModuleSample/modules')
##import mo

#from mod1 import suml as sum_list, prodl as multi_list

my_list = [i + 1 for i in range(5)]
# print("Calling module's function: ", mod1.suml(my_list))
# print("Calling module's function: ", mod1.prodl(my_list))
# print(mod1.suml(my_list) == 15)
# print(mod1.prodl(my_list) == 120)

# print("Calling module's function: ", suml(my_list))
# print("Calling module's function: ", prodl(my_list))
# print(suml(my_list) == 15)
# print(prodl(my_list) == 120)

# print("Calling module's function: ", sum_list(my_list))
# print("Calling module's function: ", multi_list(my_list))
# print(sum_list(my_list) == 15)
# print(multi_list(my_list) == 120)