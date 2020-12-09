import os

def files(suffix, path):
    if suffix == "" or path == "":
        return
    directories = []
    find_files(suffix, path, directories)
    return directories

def find_files(suffix, path, directories):
    for d in os.listdir(path):
        current = os.path.join(path, d)
        if os.path.isfile(current):
            if current.endswith(suffix):
                directories.append(current)
        elif os.path.isdir(current):
            find_files(suffix, current, directories)


print(files("t1.c", "./testdir"))
#print(files("", "./testdir"))
#print(files("fakeFile", './testdir'))

