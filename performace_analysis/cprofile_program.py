import os

# to check the time spent on each function and method , how many times each of them called
# you can use cProfile to get to know how often and for how long various parts of the program executed.

# commands to run the cProfile python -m cProfile program.py

os.system("python -m cProfile decorator_to_time_analysis.py")

'''
output 


Total time taken to complete the function random_sort:1.69267511368
         2000312 function calls (2000301 primitive calls) in 1.761 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 __future__.py:48(<module>)
        1    0.000    0.000    0.000    0.000 __future__.py:74(_Feature)
        7    0.000    0.000    0.000    0.000 __future__.py:75(__init__)
        8    0.000    0.000    0.000    0.000 _weakrefset.py:16(__init__)
        8    0.000    0.000    0.000    0.000 _weakrefset.py:20(__enter__)
        8    0.000    0.000    0.000    0.000 _weakrefset.py:26(__exit__)
       19    0.000    0.000    0.000    0.000 _weakrefset.py:36(__init__)
        8    0.000    0.000    0.000    0.000 _weakrefset.py:52(_commit_removals)
       19    0.000    0.000    0.000    0.000 _weakrefset.py:58(__iter__)
        9    0.000    0.000    0.000    0.000 _weakrefset.py:70(__contains__)
       16    0.000    0.000    0.000    0.000 _weakrefset.py:83(add)
        8    0.000    0.000    0.000    0.000 abc.py:105(register)
        8    0.000    0.000    0.000    0.000 abc.py:148(__subclasscheck__)
        4    0.000    0.000    0.000    0.000 abc.py:86(__new__)
        4    0.000    0.000    0.000    0.000 abc.py:89(<genexpr>)
        1    0.000    0.000    0.000    0.000 cProfile.py:5(<module>)
        1    0.000    0.000    0.000    0.000 cProfile.py:66(Profile)
        1    0.058    0.058    1.761    1.761 decorator_to_time_analysis.py:1(<module>)
        1    0.276    0.276    1.693    1.693 decorator_to_time_analysis.py:32(random_sort)
        1    0.000    0.000    0.000    0.000 decorator_to_time_analysis.py:7(check_time)
        1    0.000    0.000    1.693    1.693 decorator_to_time_analysis.py:8(function_timer)
        1    0.000    0.000    0.000    0.000 functools.py:17(update_wrapper)
        1    0.000    0.000    0.000    0.000 functools.py:39(wraps)
        6    0.000    0.000    0.000    0.000 hashlib.py:100(__get_openssl_constructor)
        1    0.003    0.003    0.003    0.003 hashlib.py:56(<module>)
        1    0.001    0.001    0.001    0.001 io.py:34(<module>)
        1    0.000    0.000    0.000    0.000 io.py:69(IOBase)
        1    0.000    0.000    0.000    0.000 io.py:73(RawIOBase)
        1    0.000    0.000    0.000    0.000 io.py:76(BufferedIOBase)
        1    0.000    0.000    0.000    0.000 io.py:79(TextIOBase)
        1    0.000    0.000    0.000    0.000 pstats.py:1(<module>)
        1    0.000    0.000    0.000    0.000 pstats.py:32(Stats)
        1    0.000    0.000    0.000    0.000 pstats.py:451(TupleComp)
        1    0.000    0.000    0.001    0.001 random.py:100(seed)
        1    0.006    0.006    0.010    0.010 random.py:40(<module>)
        1    0.000    0.000    0.000    0.000 random.py:655(WichmannHill)
        1    0.000    0.000    0.000    0.000 random.py:72(Random)
        1    0.000    0.000    0.000    0.000 random.py:805(SystemRandom)
        1    0.000    0.000    0.001    0.001 random.py:91(__init__)
        1    0.000    0.000    0.000    0.000 {_hashlib.openssl_md5}
        1    0.000    0.000    0.000    0.000 {_hashlib.openssl_sha1}
        1    0.000    0.000    0.000    0.000 {_hashlib.openssl_sha224}
        1    0.000    0.000    0.000    0.000 {_hashlib.openssl_sha256}
        1    0.000    0.000    0.000    0.000 {_hashlib.openssl_sha384}
        1    0.000    0.000    0.000    0.000 {_hashlib.openssl_sha512}
        1    0.000    0.000    0.000    0.000 {binascii.hexlify}
        4    0.000    0.000    0.000    0.000 {built-in method __new__ of type object at 0x7fff87164458}
        1    0.000    0.000    0.000    0.000 {function seed at 0x1051f4a28}
       35    0.000    0.000    0.000    0.000 {getattr}
        6    0.000    0.000    0.000    0.000 {globals}
        8    0.000    0.000    0.000    0.000 {isinstance}
    27/16    0.000    0.000    0.000    0.000 {issubclass}
        1    0.000    0.000    0.000    0.000 {math.exp}
        2    0.000    0.000    0.000    0.000 {math.log}
        1    0.000    0.000    0.000    0.000 {math.sqrt}
        8    0.000    0.000    0.000    0.000 {method '__subclasses__' of 'type' objects}
        8    0.000    0.000    0.000    0.000 {method '__subclasshook__' of 'object' objects}
       24    0.000    0.000    0.000    0.000 {method 'add' of 'set' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        4    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
  2000000    0.148    0.000    0.148    0.000 {method 'random' of '_random.Random' objects}
        8    0.000    0.000    0.000    0.000 {method 'remove' of 'set' objects}
        1    0.000    0.000    0.000    0.000 {method 'union' of 'set' objects}
        1    0.000    0.000    0.000    0.000 {method 'update' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 {posix.urandom}
        1    0.056    0.056    0.056    0.056 {range}
        3    0.000    0.000    0.000    0.000 {setattr}
        1    1.213    1.213    1.213    1.213 {sorted}
        2    0.000    0.000    0.000    0.000 {time.time}






'''