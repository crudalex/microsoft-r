class LRUCache:

    def __init__(self, capacity):
        self.dict = {}
        self.list = []
        self.max = capacity
        return

    def get(self, key):
        val = self.dict.get(key)
        if val is None:
            return -1

        if key in self.list:
            self.list.pop(self.list.index(key))
            self.list.append(key)
        else:
            self.evict()
            self.list.append(key)

        return val

    def put(self, key, value):

        if key in self.dict:
            self.dict[key] = value
            self.list.pop(self.list.index(key))
            self.list.append(key)
        else:
            self.evict()
            self.list.append(key)
            self.dict[key] = value

    def evict(self):
        if len(self.dict) == self.max:
            item = self.list.pop(0)
            del self.dict[item]

if __name__ == '__main__':
    cache = LRUCache(2)

    cache.put(2, 1);
    cache.put(1, 1);
    cache.put(2, 3);
    cache.put(4, 1);

    cache.get(1);
    cache.get(2);
