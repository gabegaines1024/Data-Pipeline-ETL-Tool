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
        self.cache.move_to_end(key)
        return self.cache[key] = (value, self.ttl)

    #remember to store this into a time stamp so you can use it in the check_time_stamp function
    def cache_time_stamp() -> int:
        timeStamp = time.time()
        return timeStamp

    def check_time_stamp(self, storedTimeStamp: int) -> Optional[int]:
         currentTime = time.time()
         age = currentTime - storedTimeStamp

         return age > self.ttl ? 0 : 1 

    def get(self, key: str) -> Any:
        """
        Get value, returns None if not found or expired.
        
        TODO:
        1. Check if key exists (if not, increment misses and return None)
        2. Get value and timestamp from cache
        3. Check if expired (current time - timestamp > ttl)
        4. If expired, delete and return None
        5. Move to end (most recently used)
        6. Increment hits
        7. Return value
        
        Hint: Store as (value, timestamp) tuple in cache
        Hint: Use time.time() for current timestamp
        """
        if key not in self.cache.keys():
            self.misses += 1
            return "Key is invalid"


    def clear(self) -> None:
