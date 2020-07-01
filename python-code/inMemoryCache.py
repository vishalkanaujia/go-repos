'''
Implement an in-memory caching library to store (key, value) objects for faster retrieval. Key requirements of the library are as follows:

The Cache will have fixed capacity specified at initialization time to limit memory usage
Storage and retrieval from Cache should be fast
Cache should support efficient replacement based on configurable eviction policy (eg. LRU - Least Recently Used) when trying to insert in a full cache
Support expiry of cache entries based on TTL (time to live in seconds) value specified at time of cache insert.
'''
from time import time

class CacheEntry:
    def __init__(self, value, ttl, node):
        self.value = value
        self.expiresAt = time() + ttl
        self.isExpired = False
        self.LRUNode = node
        
    def expired(self):
        if self.isExpired is False:
            return self.expiresAt < time()
        return self.isExpired

class LRUNode:
    def __init__(self, key):
        self.key = key
        self.next = None
        self.prev = None

class LRUList:
    def __init__(self):
        self.head = None
        self.last = None
        
    def LRUUpdate(self, key):
        node = LRUNode(key)
           
        if self.head is None:
            self.head = node
            self.last = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
        return node
    
    def LRUDelete(self):
        #print("last node=", self.last.key)
        if self.last is not None:
            last = self.last
            key = last.key
            self.last.prev.next = None
            self.last = self.last.prev
            del last
            return key

    def LRUDeleteSingleNode(self, node):
        if node.next is not None:
            node.next.prev = node.prev
        if node.prev is not None:
            node.prev.next = node.next


class MemCache:
    def __init__(self, size):
        self.mcache = {}
        self.size = size
        self.lru = LRUList()
        
    def mSet(self, key, value, ttl=30):
        curSize = len(self.mcache)
            
        if curSize < self.size:
            node = self.lru.LRUUpdate(key)
            entry = CacheEntry(value, ttl, node)
            self.mcache.setdefault(key, entry)
        else:
            self.mEvict()
            return self.mSet(key, value, ttl)

    def mGet(self, key):
        if key in self.mcache:
            entry = self.mcache[key]
            print(entry)
            if entry.expired():
                return (-1, "expired")
            
            self.lru.LRUUpdate(key)
            return (0, entry.value)
        
        return (-1, "not found")
    
    def mEvict(self):
        key = self.lru.LRUDelete()
        #print("deleting key=", key)
        del self.mcache[key]
    
    def mDel(self, key):
        if key in self.mcache:
            node = self.mcache[key].LRUNode
            self.lru.LRUDeleteSingleNode(node)
            del self.mcache[key]
            
mcache = MemCache(2)
mcache.mSet("k1", 1)
mcache.mSet("k2", 2)
mcache.mSet("k3", 3)
mcache.mDel("k2")
mcache.mSet("k5", 5, 0)


# tests
#print(mcache.mcache)

err, value = mcache.mGet("k1")
assert(err == -1)
err, value = mcache.mGet("k2")
assert(err ==-1)
err, value = mcache.mGet("k3")
assert(err == 0)


err, value = mcache.mGet("k5")
assert(err == -1)