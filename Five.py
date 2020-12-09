import hashlib, time

class Block:
    def __init__(self, timestamp, data, previous_hash, next_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.next = next_hash
      self.hash = self.calc_hash(data)
    def calc_hash(self, data: str):
        sha = hashlib.sha256()
        hash_str = data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

class Blockchain:
    def __init__(self):
        self.head = None
        self.tail = None
    def create_block(self, data):
        return Block(time.gmtime(), data, None, None)
    def add_block(self, hashInfo):
        if hashInfo == "":
            return
        if self.head is None:
            block = self.create_block(str(hashInfo))
            self.head = block
            self.tail = block
        else:
            block = self.create_block(str(hashInfo))
            block.next = self.tail
            self.tail.previous_hash = block
            self.tail = block
    def __str__(self):
        s = ""
        block = self.tail
        while block is not None:
            s += f"Block - hash({block.hash}) - data({block.data}) - prev_hash({block.previous_hash})\n"
            block = block.next
        return s

blockChain = Blockchain()
blockChain.add_block("String")
blockChain.add_block("Two")
blockChain.add_block("Three")
print(blockChain)

blockChain = Blockchain()
blockChain.add_block("")
blockChain.add_block("Two")
blockChain.add_block("Three")
print(blockChain)

blockChain = Blockchain()
blockChain.add_block(23214)
blockChain.add_block("Two")
blockChain.add_block("Three")
print(blockChain)
