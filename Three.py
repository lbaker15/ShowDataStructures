import heapq, sys

class Node(object):
    def __init__(self, char=None, freq=None):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    def __lt__(self, value):
        return self.freq < value.freq
    def __eq__(self, value):
        return self.freq == value.freq

def huffman(data: str):
    if data == None or data == "":
        return None, None
    def loop_char(data: str):
        chars = {}
        for char in data:
            if char in chars.keys():
                chars[char] += 1
            else:
                chars[char] = 1
        return chars
    def push_to_heap(data: dict):
        sort_data = sorted(data.items(), key=lambda x: x[1])
        h = []
        for item in sort_data:
            new_node = Node(item[0], item[1])
            heapq.heappush(h, ( item[1], new_node ))
        return h
    def init_tree(h):
        while(len(h) > 1):
            right_item = heapq.heappop(h)
            left_item = heapq.heappop(h)
            new_node = Node(freq=(left_item[1].freq + right_item[1].freq))
            new_node.left = left_item[1]
            new_node.right = right_item[1]
            heapq.heappush(h, (new_node.freq, new_node))
        return h[0][1]
    def binary_char(root, obj, str):
        if root:
            binary_char(root.left, obj, str + "0")
            binary_char(root.right, obj, str + "1")
            if root.char:
                obj[root.char] = str

    characters = loop_char(data)
    heap = push_to_heap(characters)
    tree = init_tree(heap)
    char = {}
    binary_char(tree, char, "")
    for key, value in char.items():
        data = data.replace(key, value)
    return data, tree, characters

def decode(string, tree):
    decode = ""
    if string == None:
        return
    n = len(string)
    count = 0
    while count < n:
        current = tree
        while current.left is not None and current.right is not None:
            if string[count] == "0":
                current = current.left
            else:
                current = current.right
            count += 1
        decode += current.char
    return decode, tree, string


"""
#Test One
a_great_sentence = "This is a sentence"
print("Content of the data is: {}\n".format(a_great_sentence))
data = huffman(a_great_sentence)
print("Content of the encoded data is: {}\n".format(data))
decoded = decode(data[0], data[1])
print("Content of the decoded data is: {}\n".format(decoded))

#Test Two
another_sent = ""
print("Content of the data is: {}\n".format(another_sent))
data_two = huffman(another_sent)
print("Content of the encoded data is: {}\n".format(data_two))
decoded_two = decode(data_two[0], data_two[1])
print("Content of the decoded data is: {}\n".format(decoded_two))
"""
#Test Three
another_sent = "OneWord"
print("Size of string: {}\n".format(sys.getsizeof( another_sent )) )
print("Content of the data is: {}\n".format(another_sent))
data_two = huffman(another_sent)
print("The size of the encoded data is: {}\n".format(sys.getsizeof( int(data_two[0], base=2) )))
print("Content of the encoded data is: {}\n".format(data_two))
decoded_two = decode(data_two[0], data_two[1])
print("The size of the decoded data is: {}\n".format(sys.getsizeof( str(decoded_two[0]) )))
print("Content of the decoded data is: {}\n".format(decoded_two))



