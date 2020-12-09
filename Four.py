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
    def get_child_index(self):
        if len(self.groups) != 0:
            if self.index < len(self.groups) - 1 or self.index == len(self.groups) - 1:
                return self.groups[self.index]
            else:
                return "Falsify"
        else:
            return None
    def increment_index(self):
        self.index += 1

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
    def set(self, value):
        self.visited.append(value)
    def pop(self):
        self.visited.pop(0)

def is_user(user, group):
    stack = Stack()
    state = State()
    stack.push(group)
    while group:
        if group.get_child_index() == "Falsify":
            return False
        if group not in state.visited:
            if user in group.get_users():
                return True
        if group.get_child_index() is not None:
            group = group.get_child_index()
            stack.push(group)
        else:
            stack.pop()
            group = stack.top()
            group.increment_index()


"""
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
print("User is in group:", is_user("new_user", child))

parent = Group("parent")
parent.add_user("parent_user")
child = Group("child")
parent.add_group(child)
sub_child = Group("subchild")
child.add_group(sub_child)
print("User is in group:", is_user("parent_user", child))

parent = Group("parent")
parent.add_user("parent_user")
child = Group("child")
parent.add_group(child)
sub_child = Group("subchild")
child.add_group(sub_child)
print("User is in group:", is_user("doesnt_exist", child)) 
"""

parent = Group("parent")
parent.add_user("parent_user")
child = Group("child")
parent.add_group(child)
sub_child = Group("subchild")
child.add_group(sub_child)
print("User is in group:", is_user("", child))

