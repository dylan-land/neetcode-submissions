class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.queue = []
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.queue.remove(key)
            self.queue.append(key)
            self.cache[key] = value
        else:
            self.cache[key] = value
            self.queue.append(key)
            
            if len(self.queue) > self.capacity:
                removal = self.queue.pop(0)
                del self.cache[removal]

