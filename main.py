import time
current_time = time.time()
#print(current_time)

f_f_t = 0
s_f_t = 0

def speed_calc_decorator(function):
    def wrapper_function():
        f_t = time.time()
        function()
        e_t = time.time()
        print(f"Run speed of {function.__name__} :{ e_t - f_t}")
    return wrapper_function

@speed_calc_decorator 
def fast_function():
    for i in range(10000000):
        i * i

@speed_calc_decorator 
def slow_function():
    for i in range(100000000):
        i * i

if __name__ == '__main__': 
    fast_function()
    slow_function()

