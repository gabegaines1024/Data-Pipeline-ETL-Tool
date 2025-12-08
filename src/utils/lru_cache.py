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
            self.cache[key] = (value, tistamp)
            self.cache.move_to_end(key)
        
        #check the capacity and add the key
        if (len(self.cache) >= self.capacity):
            #removes the last item (least recently used)
            self.cache.popitem(last=False)
        
        #lastly add the key
        self.cache[key] = (value, timestamp)

    def get(self, key: str) -> Any:     
        #check if the key is in the cache
        if key not in self.cache.keys():
            self.misses += 1
            return "Key is invalid"
        
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

    def stats(self, name: str) -> dict:
        total = self.hits + self.misses
        hit_rate = (self.hits / total * 100) if total > 0 else 0

        return {
            f"{name.upper()} Cache Stats": {
                "size": len(self.cache),
                "capacity": self.capacity,
                "hits": self.hits,
                "misses": self.misses,
                "hit_rate_percent": hit_rate,
            }
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
       self.cache = OrderedDict()
       self.cache_size = cache_size
       self.ttl = ttl
    
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
        md5_hash = hashlib.md5()
        md5_hash.update(json_data.encode('utf-8'))
        return md5_hash.hexdigest()
         
    def get(self, url: str, params: dict = None) -> Any:
        """
        Get data with caching.
        
        Args:
            url: API endpoint URL
            params: Query parameters
            
        Returns:
            Cached or fresh API response
        
        TODO:
        1. Generate cache key
        2. Try to get from cache
        3. If cache hit, return cached data
        4. If cache miss, return None (actual API call in api_extractor.py)
        """
        pass
    
    def cache_stats(self) -> dict:
        """Get cache statistics."""
        # TODO: Return self.cache.stats()
        pass
