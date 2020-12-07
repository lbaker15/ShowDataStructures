class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []
        self.index = 0
    def add_group(self, group):
        self.groups.append(group)
    def add_user(self, user):
        self.users.append(user)
    def get_groups(self):
        return self.groups
    def get_users(self):
        return self.users
    def get_name(self):
        return self.name
    def get_child(self):
        if len(self.groups) != 0:
            return self.groups[self.index]
        else:
            return None
    def get_child_index(self):
        if len(self.groups) != 0:
            return self.groups[self.index]
        else:
            return None
    def increment_index(self):
        self.index += 1
    #index, increment, get child via index

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")
sub_child_two = Group("subchildTwo")
sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)
child.add_group(sub_child)
child.add_group(sub_child_two)
new_user = "new_user"
sub_child_two.add_user(new_user)
parent.add_group(child)

class Stack:
    def __init__(self, initial_size=3):
        self.list = list()
    def push(self, data):
        self.list.append(data)
    def pop(self):
        self.list.pop()
    def top(self):
        return self.list[len(self.list) - 1]
    #pop top isEmpty
    def __repr__(self):
        if len(self.list) > 0:
            s = "<top of stack>\n_________________\n"
            s += "\n_________________\n".join([str(item.name) for item in self.list[::-1]])
            s += "\n_________________\n<bottom of stack>"
            return s

class State(object):
    def __init__(self):
        self.visited = []
        #list visited groups, set and get visited
    def set(self, value):
        self.visited.append(value)
    def pop(self):
        self.visited.pop(0)


def is_user(user, group):
    stack = Stack()
    state = State()
    stack.push(group)
    while group:
        if group not in state.visited:
            print(group.name)
            if user in group.get_users():
                print( True )
            state.set(group)
        if group.get_child_index() != None:
            group = group.get_child_index()
            stack.push(group)
        else:
            stack.pop()
            group = stack.top()
            group.increment_index()





            """
            print("Before child:", group.name)
            #Get group child
            group = group.get_child_index(0)
            #Check if group child visited before
            if group not in state.visited.keys():
                print("Not in state")
                if group == None:
                    print(False)
                else:
                    print(group.name)
                    state.set(group)
            else:
                #Been visited
                print("STATE", state)
                group.increment_index()
                state.pop(group)
            """



is_user("new_user", child)


