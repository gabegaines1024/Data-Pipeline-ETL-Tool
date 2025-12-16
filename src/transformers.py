"""Data transformers for cleaning and enriching data."""
from typing import Optional
from .models import DataRecord


class StringCleaner:
    """
    Clean string fields (strip whitespace, lowercase, etc.).
    """
    
    def __init__(self, strip: bool = True, lowercase: bool = False):
        self.strip = strip
        self.lowercase = lowercase
        pass
    
    def transform(self, record: DataRecord) -> Optional[DataRecord]:
        """
        Clean all string fields in the record.
        """
        for key, value in record.data.items():
            if isinstance(value, str):
                if self.strip:
                    value = value.strip()
                if self.lowercase:
                    value = value.lower()


class FilterTransformer:
    """
    Filter records based on a condition.
    """
    
    def __init__(self, condition_func):
        self.condition_func = condition_func
    
    def transform(self, record: DataRecord) -> Optional[DataRecord]:
        """
        Apply filter condition.
        """
        return record if self.condition_func(record) else None

