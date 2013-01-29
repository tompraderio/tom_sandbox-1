import os

def file_create(filename, *args):
    with open(filename, 'a') as f: pass
    return "Created file {}.".format(filename)

def file_read(filename, *args):
    with open(filename, 'r') as f:
        return f.read()

def file_update(filename, *args):
    string = ' '.join(args)
    with open(filename, 'w') as f:
        f.write(string)
    return "Wrote string '{}' to file {}".format(string, filename)

def file_delete(filename, *args):
    os.remove(filename)
    return "Deleted file {}.".format(filename)


#update foo.txt my dick
# ['update', 'foo.txt', 'my', 'dick']
__file_funcs = {
    "create": file_create,
    "read": file_read,
    "update": file_update,
    "delete": file_delete,
    }

def get_func(name):
    return __file_funcs.get(name, lambda fn, *args: None)
