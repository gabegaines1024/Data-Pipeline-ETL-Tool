"""Simple data models for the ETL pipeline."""
from dataclasses import dataclass, field
from typing import Any, Dict
from datetime import datetime


@dataclass
class DataRecord:
    """
    Represents a single data record.
    
    TODO: Implement methods to:
    1. Get field values safely
    2. Set field values
    """
    data: Dict[str, Any]
    source: str = "unknown"
    timestamp: datetime = field(default_factory=datetime.now)
    
    def get(self, key: str, default: Any = None) -> Any:
        """
        Get a field value.
        
        TODO: Return data[key] if exists, else default
        """
        pass
    
    def set(self, key: str, value: Any) -> None:
        """
        Set a field value.
        
        TODO: Set data[key] = value
        """
        pass

