import time

def decorator_function(function):
    def wrapper_function():
        time.sleep(2)
        function()
    return wrapper_function

@decorator_function
def say_hello():
    print("Hello")

def say_world():
    print("World")
    
def say_day():
    print("Day")

xinjang = decorator_function(say_day)

print(xinjang())