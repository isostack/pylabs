def add(*args):
    return sum(args)

#print(add(2,4,5))

def calculate(**kwargs):
    for key,value in kwargs.items():
        print(value)
    print(kwargs["add"])

calculate(add = 3 , multiply = 5)
