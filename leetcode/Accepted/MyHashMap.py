class MyHashMap(object):

    buckets = []
    size = 100000

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.buckets = [ None for _ in range(self.size)]

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        index = self._hash(key)
        self.buckets[index] = value

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        index = self._hash(key)
        value = self.buckets[index]
        if value == None:
            return -1
        return value

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        index = self._hash(key)
        self.buckets[index] = None

    def _hash(self, key):
        return key % self.size

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
if __name__ == '__main__':
    hashMap = MyHashMap()
    hashMap.put(1, 1)
    hashMap.put(2, 2)
    assert 1 == hashMap.get(1)
    assert -1 == hashMap.get(3)
    hashMap.put(2, 1)
    assert 1 == hashMap.get(2)
    hashMap.remove(2)
    assert -1 == hashMap.get(2)
