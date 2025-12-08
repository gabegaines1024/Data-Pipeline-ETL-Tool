"""
LRU Cache for API responses and expensive operations 

Implementing a LRU cache with TTL support for the ETL pipeline
"""

from collections import OrderedDict
from typing import Any, Optional
import time
import hashlib
import json
import time

class LRUCache:
    """LRU Cache with optional TTL (time-to-live) support"""

    def __init__(self, capacity: int, ttl: Optional[int] = None):
        if(capacity) <= 0:
            raise ValueError("Capacity must be greater than 0!")
        self.capacity = capacity
        self.ttl = ttl
        self.cache = OrderedDict()
        self.misses = 0
        self.hits = 0
    
    def put(self, key: str, value: Any) -> Any:
        """Add or update key-value pair"""
        timestamp = time.time()

        #if key exists update
        if key in self.cache:
            self.cache[key] = (value, timestamp)
            self.cache.move_to_end(key)
            return 
        
        #check the capacity and add the key
        if (len(self.cache) >= self.capacity):
            #removes the last item (least recently used)
            self.cache.popitem(last=False)
        
        #lastly add the key
        self.cache[key] = (value, timestamp)

    def get(self, key: str) -> Any:     
        #check if the key is in the cache
        if key not in self.cache:
           self.misses += 1
           return None
        
        #store the value, timestamp as a tuple
        value, timestamp = self.cache[key]

        #if key has ttl, check if it is expired
        if self.ttl is not None and (time.time() - timestamp >= self.ttl):
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

    def stats(self) -> dict:
        total = self.hits + self.misses
        hit_rate = (self.hits / total * 100) if total > 0 else 0

        return {
    'size': len(self.cache),
    'capacity': self.capacity,
    'hits': self.hits,
    'misses': self.misses,
    'hit_rate': f'{hit_rate:.2f}%'
}

    def __len__(self):
        """return the size of the cache"""
        return len(self.cache)

    def __contains__(self, key):
        """Support 'in' Operator"""
        return key in self.cache

    def __repr__(self):
        """return string representation"""
        return f"LRUCache(cache={list(self.cache.keys())}, capacity={self.capacity})"

class CachedAPIClient:
    """API client with automatic caching for ETL pipeline."""
    
    def __init__(self, cache_size: int = 100, ttl: int = 300):
       self.cache = LRUCache(cache_size, ttl)
       

    def _make_cache_key(self, url: str, params: dict = None) -> str:
        """
        Generate cache key from URL and parameters.
        """ 
        #key to recognize a parameters and url
        key_data = {
                'url': url,
                'params': params or {}   
                }

        #convert to JSON string(sorted keys for consistency)
        json_data = json.dumps(key_data, sort_keys=True)

        #hash with MD5 and return
        hash_object = hashlib.md5(json_data.encode('utf-8'))
        return hash_object
         
    def get(self, url: str, params: dict = None) -> Any:
        """
        Get data with caching.
        """

        #generate cache key
        key = self._make_cache_key(url, params)
        
        #try cache first
        cached_response = self.cache.get(key)
        if cached_response is not None:
            print(f"Cache HIT for {url}")
            return cached_response
        #Cache miss - make actual API request
        print(f"Cache MISS for {url} - fetching from API...")

     #Test your implementation
if __name__ == "__main__":
    print("=== Testing LRU Cache ===\n")
    
    # Test 1: Basic operations
    cache = LRUCache(capacity=3)
    cache.put("user:1", {"name": "Alice", "age": 30})
    cache.put("user:2", {"name": "Bob", "age": 25})
    cache.put("user:3", {"name": "Charlie", "age": 35})
    
    print(f"Cache size: {len(cache)}")
    print(f"Get user:1: {cache.get('user:1')}")
    print()
    
    # Test 2: Eviction
    cache.put("user:4", {"name": "David", "age": 40})
    print(f"After adding user:4, user:2 should be evicted")
    print(f"Get user:2: {cache.get('user:2')}")
    print()
    
    # Test 3: TTL expiration
    cache_ttl = LRUCache(capacity=5, ttl=2)  # 2 second TTL
    cache_ttl.put("temp", "data")
    print(f"Get temp immediately: {cache_ttl.get('temp')}")
    
    time.sleep(3)
    print(f"Get temp after 3 seconds: {cache_ttl.get('temp')}")
    print() 
   
    #Test 4: Cache Statistics
    print("Cache Stats: ")
    print(cache.stats())
    print()

    # Test 5: Cached API Client
    api_client = CachedAPIClient(cache_size=10, ttl=300)
    
    # Simulate caching API calls
    key = api_client._make_cache_key("https://api.example.com/users", {"id": 123})
    print(f"Cache key: {key}")
