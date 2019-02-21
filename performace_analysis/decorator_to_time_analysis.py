import time
from functools import wraps
import random

def check_time(function):
    @wraps(function)
    def function_timer(*args,**kwargs):
        time0= time.time()
        result = function(*args,**kwargs)
        time1 = time.time()
        print("Total time taken to complete the function %s:%s" %(function.func_name, str(time1-time0)))
        return result
    return function_timer

@check_time
def random_sort(n):
    return sorted([random.random() for i in range(int(n))])

if __name__ == "__main__":
    random_sort(2000000)
