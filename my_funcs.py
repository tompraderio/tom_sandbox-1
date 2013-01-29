def __print_func(*strings):
    return ' '.join(strings)

def __add(*numbers):
    ints = (int(n) for n in numbers)
    return sum(ints)

def __do_nothing(*args):
    return None

__funcs = {
    "print": __print_func,
    "add": __add,
    }

def get_func(name):
    return __funcs.get(name, __do_nothing)
