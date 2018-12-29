import time
from functools import wraps
import random

import cProfile,pstats,io

def check_time(function):
    @wraps(function)
    def function_timer(*args,**kwargs):
        time0= time.time()
        result = function(*args,**kwargs)
        time1 = time.time()
        print("Total time taken to complete the function %s:%s" %(function.func_name, str(time1-time0)))
        return result
    return function_timer

def profiler(function):

    def inner(*args,**kwargs):
        pr = cProfile.Profile()
        pr.enable()
        result = function(*args,**kwargs)
        pr.disable()
        s = io.StringIO()
        #sortby = 'cumulative'
        ps = pstats.Stats(pr,stream=s).sort_stats('cumulative')
        ps.print_stats()
        print(s.getvalue())
        return result
    return inner

@check_time
def random_sort(n):
    return sorted([random.random() for i in range(int(n))])

if __name__ == "__main__":
    random_sort(2000000)
