class Node:                            # Doubly linked list for keeping track the least recently used and most recently used keys
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRU_Cache:
    def __init__(self, cap):    #Initialize the LRU cache with positive size capacity.
        if not 50 >= cap >= 0:
            raise ValueError("Capacity must be in between 0 and 50")
        self.capacity = cap
        self.cache = {}
        self.left = self.right = Node(None, None)   #making two nodes "left" and "right"
        self.left.next = self.right            #linking both nodes
        self.right.prev = self.left
        self.miss = 0
        self.total = 0        #total refrences
    def remove_lru(self):                 #removes the least recently used key in cache and node in linked list
        prev_node = self.left
        next_node = self.left.next
        self.cache.pop(next_node.key)
        prev_node.next = next_node.next
        next_node.next.prev = prev_node
    def remove(self, n):      #removes the node from linked list
        prev_node = n.prev
        next_node = n.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def insert_mru(self, n):         #makes the key most recenty used
        next_node = self.right
        prev_node = self.right.prev
        prev_node.next = n
        next_node.prev = n
        n.prev = prev_node
        n.next = next_node

    def get(self, key):      #returns the value of the key if it is exist otherwise returns -1
        self.total += 1
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert_mru(self.cache[key])
            return self.cache[key].val
        self.miss += 1
        return -1

    def put(self, key, val):     # Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
        self.total += 1
        if not (0 <= key <= 100 and 0 <= val <= 100):
            raise ValueError("key and value must be in between 0 and 100")
        if key in self.cache:
            self.remove(self.cache[key])
        else:
            if len(self.cache)<self.capacity:
                self.miss += 1
        self.cache[key] = Node(key,val)
        self.insert_mru(self.cache[key])
        if len(self.cache) > self.capacity:
            self.remove_lru()
            self.miss += 1

    def calc_miss_rate(self):     #calculates the miss rate by dividing miss count by total refrences
        self.miss_rate = round((self.miss/self.total)*100,2)
        return self.miss_rate

    def print_cache(self):   #prints the cache in a dictionary format
        current = self.left.next
        print("{", end="")
        for i in range(self.capacity):
            print(f"{current.key},{current.val},",end="")
            if i == self.capacity/2:
                print()
            current = current.next
        print("}")


print("""\n\nTesting the LRU_Cache by providing \nInput:
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]\nOutput:""")
Cache1=LRU_Cache(2)
Cache1.put(1,1)
Cache1.put(2,2)
# print(Cache1.get(1))
Cache1.put(3,3)
print(Cache1.get(2))
# Cache1.put(4,4)
# print(Cache1.get(1))
# print(Cache1.get(3))
# print(Cache1.get(4))
print(f"miss: {Cache1.miss}  TOTAL: {Cache1.total}")
print(f"miss rate: {Cache1.calc_miss_rate()}")

Cache2 = LRU_Cache(50)
print("\n\nLRU Cache after filling with keys from 0 to 49")
for i in range(Cache2.capacity):
    Cache2.put(i,i)
Cache2.print_cache()
print(f"Miss={Cache2.miss}    Total={Cache2.total}")
print(f"Miss rate = {Cache2.calc_miss_rate()}%")

print("\n\nLRU Cache after retrieving odd number key-values")
for i in range(1,50,2):
    Cache2.get(i)
Cache2.print_cache()
print(f"Miss={Cache2.miss}    Total={Cache2.total}")
print(f"Miss rate = {Cache2.calc_miss_rate()}%")

print("\n\nLRU Cache after refilling it with prime number keys from 0 to 100")
prime_nos = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
for i in prime_nos:
    Cache2.put(i,i)

Cache2.print_cache()
print(f"Miss={Cache2.miss}    Total={Cache2.total}")
print(f"Miss rate = {Cache2.calc_miss_rate()}%")