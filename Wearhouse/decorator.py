from calendar import prcal


class User():
    def __init__(self, name):
        self.name = name
        self.is_online = False

# loggin decorator
def log_function_data(function):
    def wrapper(*args, **kwargs):
        print(f"You are about to call {function.__name__}{args}")
        for i in args:
            print(f"Here is the data: {i.name}")
        return(function(*args, **kwargs))
    return wrapper

def online_decorator(function):
    def wrapper(*args , **kwargs):
        if args[0].is_online:
            function(args[0])
        else:
            print("Sorry, this user is currently offline.")
    return wrapper

@log_function_data
@online_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")

new_user = User("Ed")
new_user.is_online = False

create_blog_post(new_user)