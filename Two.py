import os

def files(suffix, path):
    directories = []
    find_files(suffix, path, directories)
    return directories

def find_files(suffix, path, directories):
    print(directories)
    for d in os.listdir(path):
        current = os.path.join(path, d)
        if os.path.isfile(current):
            if current.endswith(suffix):
                directories.append(current)
        elif os.path.isdir(current):
            find_files(suffix, current, directories)


print(files("t1.c", "./testdir"))



