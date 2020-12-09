class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    def __repr__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.arr = []
    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            self.arr.append(self.head)
            return
        node = self.head
        while node.next:
            node = node.next
        append_me = Node(value)
        node.next = append_me
        self.arr.append(append_me)
    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next
        return size

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

def intersection(llist_1, llist_2):
    array = set()
    toReturn = set()
    for x in llist_1.arr:
        array.add(x.value)
    for y in llist_2.arr:
        if y.value in array:
            toReturn.add(y.value)
    newLinked = LinkedList()
    for value in toReturn:
        newLinked.append(value)
    if len(toReturn) == 0:
        return None
    return newLinked


def union(llist_1, llist_2):
    array = set()
    for x in llist_1.arr:
        if x.value not in llist_2.arr:
            array.add(x.value)
    for x in llist_2.arr:
        if x.value not in array:
            array.add(x.value)
    newLinked = LinkedList()
    for value in array:
        newLinked.append(value)
    if len(array) == 0:
        return None
    return newLinked

# Test case 1
"""
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))
"""


# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))
