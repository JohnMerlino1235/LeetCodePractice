from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.items = OrderedDict()
        self.LRU = None

    def get(self, key: int) -> int:
        if self.items.__contains__(key):
            self.items[key] = self.items.pop(key)
            return self.items[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.items.__contains__(key):
            self.items.pop(key)
        elif len(self.items) == self.capacity:
            self.items.popitem(last=False)
        self.items[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)