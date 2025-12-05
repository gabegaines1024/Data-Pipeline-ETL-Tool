"""
LRU Cache for API responses and expensive operations 

Implementing a LRU cache with TTL support for the ETL pipeline
"""

from collections import OrderedDict
from typing import Any, Optional
import time
import hashlib
import json

class LRUCache:
    """LRU Cache with optional TTL (time-to-live) support"""

    def __init__(self, capacity: int, ttl: Optional[int] = None):
        if(capacity):
            capacity >= 0 ?  self.capacity = capacity : raise ValueError("Capacity must be greater than 0!")
        ttl ? self.ttl = ttl : None
        self.cache = OrderedDict()
        self.misses = 0
        self.hits = 0
    
    def put(self, key: str, value: Any) -> Any:
        """Add or update key-value pair"""
        timestamp = time.time()

        #if key exists update
        if (self.cache[key]):
            self.cache[key] = (value, timestamp)
            self.cache.move_to_end(key)
        
        #check the capacity and add the key
        if (len(self.cache) >= self.capacity):
            #removes the last item (least recently used)
            self.cache.popitem(last=False)
        
        #lastly add the key
        self.cache[key] = (value, timestamp)

    def get(self, key: str, value: Any) -> Any:     
        #check if the key is in the cache
        if key not in self.cache.keys():
            self.misses += 1
            return "Key is invalid"
        
        #store the value, timestamp as a tuple
        value, timestamp = self.cache[key]

        #if key has ttl, check if it is expired
        if self.ttl and (time.time() - timestamp < self.ttl):
            del self.cache[key]
            self.misses += 1
            return None

        #move to the end (most recently used)
        self.cache.move_to_end(key)
        self.hits += 1
        return value


    def clear(self) -> None:
        """Clear cached items"""
        self.cache.clear()
        self.misses = 0
        self.hits = 0


