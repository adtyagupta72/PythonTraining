#import main

counter = 0

print("I am inside Mod1 Module!! Yay!")
context =__name__
print(context)
if context == "__main__":
    print("Mod1 file was executed!")
else:
    print("mod1: I am acting as a module only!!")