"""Simple data models for the ETL pipeline."""
from dataclasses import dataclass, field
from typing import Any, Dict
from datetime import datetime


@dataclass
class DataRecord:
    """
    Represents a single data record.
    """
    data: Dict[str, Any] = field(default_factory=dict)
    source: str = "unknown"
    timestamp: datetime = field(default_factory=datetime.now)
    
    def get(self, key: str, default: Any = None) -> Any:
        """
        Get a field value.
        """
        return self.data.get(key, default)
    
    def set(self, key: str, value: Any) -> None:
        """
        Set a field value.
        """
        self.data[key] = value

