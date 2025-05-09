import mod1
print("I am from main file!!")
context =__name__
print(context)
if context == "__main__":
    print("Main file was executed!")
else:
    print("main.py: I am acting as a module only!!")

print("Counter: ", mod1.counter)
mod1.counter += 1
print("Counter: ", mod1.counter)