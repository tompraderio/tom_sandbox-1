from file_funcs import get_func

# This is a simple REPL function
def shell():
    while True:
        args = raw_input("$").split(" ")
        if args[0] == 'exit': break
        func = get_func(args[0])
        filename = args[1]
        print func(filename, *args[2:])


