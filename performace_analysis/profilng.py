import cProfile, pstats, io


def profileit(func):
    def inner(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        retval = func(*args, **kwargs)
        pr.disable()
        s = io.StringIO()
        sortby = 'cumulative'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
        return retval

    return inner

@profileit
def sum_list(list1):
    in_list = [(a+2) for a in list1]
    return sum(in_list)

sum_list([1,2,3,4,5,6,7])
