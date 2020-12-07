class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRU_Cache(object):
    def __init__(self, capacity: int):
        self.items = {}
        self.size_items = 0
        self.capacity = self.set_capacity(capacity)
        self.head = None
        self.tail = None
    def get(self, key):
        if key in self.items:
            return self.items[key].value
        else:
            return -1
    def set(self, key, value):
        new_node = Node(key, value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            self.size_items += 1
            self.items[key] = new_node
            return
        else:
            if self.at_capacity():
                self.remove_oldest()
                self.make_new_head(new_node, key)
            else:
                self.make_new_head(new_node, key)
            self.size_items += 1
    def at_capacity(self):
        return self.capacity < self.size_items + 1
    def make_new_head(self, new_node, key):
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node
        self.items[key] = new_node
    def remove_oldest(self):
        key = self.tail.key
        self.tail = self.tail.prev
        self.tail.next = None
        del self.items[key]
        self.size_items -= 1
    def set_capacity(self, capacity):
        if capacity < 1:
            return 1
        else:
            return capacity




our_cache = LRU_Cache(5)
our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);

our_cache.get(1)       # returns 1
our_cache.get(2)      # returns 2
our_cache.get(9)      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)
our_cache.set(7, 7)

our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
