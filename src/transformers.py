"""Data transformers for cleaning and enriching data."""
from typing import Optional
from .models import DataRecord


class StringCleaner:
    """
    Clean string fields (strip whitespace, lowercase, etc.).
    
    TODO: Implement string cleaning transformations
    """
    
    def __init__(self, strip: bool = True, lowercase: bool = False):
        """TODO: Store configuration"""
        pass
    
    def transform(self, record: DataRecord) -> Optional[DataRecord]:
        """
        Clean all string fields in the record.
        
        TODO:
        1. For each field in record.data
        2. If it's a string, apply cleaning (strip, lowercase)
        3. Return the modified record
        
        Hint: for key, value in record.data.items():
                  if isinstance(value, str):
                      if self.strip: value = value.strip()
                      if self.lowercase: value = value.lower()
                      record.data[key] = value
        """
        pass


class FilterTransformer:
    """
    Filter records based on a condition.
    
    TODO: Keep only records that match condition
    """
    
    def __init__(self, condition_func):
        """
        TODO: Store condition_func
        
        condition_func should be a function that takes a DataRecord
        and returns True to keep it, False to filter it out
        """
        pass
    
    def transform(self, record: DataRecord) -> Optional[DataRecord]:
        """
        Apply filter condition.
        
        TODO:
        1. Call self.condition_func(record)
        2. If True, return record
        3. If False, return None (filters it out)
        """
        pass

