from collections import OrderedDict


class LFUCache:

    class AccessLog:

        def __init__(self):
            self.log = OrderedDict()

        def push(self, key):
            pass

        def renew(self, key):
            pass

        def evict(self):
    def __init__(self, capacity):
        self.cache = dict()
        return

    def touch(self, key):
        pass

    def put(self, key, value):

        self.evict()
        self.cache[key] = value
        self.touch(key)
        return

    def get(self, key):
        value = self.cache.get(key)
        if not value:
            return -1
        self.touch(key)
        return value

    def evict(self):
        if not len(self.cache) == self.max:
            return

        key = self.log.pop()
        del self.cache[key]
        return




if __name__ == '__main__':
    cache = LFUCache(2)

    cache.put(2, 1);
    cache.put(1, 1);
    cache.put(2, 3);
    cache.put(4, 1);

    cache.get(1);
    cache.get(2);
