"""Data loaders for CSV and JSON output."""
import csv
import json
from pathlib import Path
from .models import DataRecord
from typing import List


class CSVLoader:
    """
    Load data to CSV file.
    """
    
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.records: List[DataRecord] = []
    
    def load(self, record: DataRecord) -> None:
        """
        Add record to buffer.
        """
        self.records.append(record)
    
    def save(self) -> None:
        """
        Write all buffered records to CSV file.
        """
        Path(self.filepath).parent.mkdir(parents=True, exist_ok=True)
        fieldnames = list(self.records[0].data.keys())
        with open(self.filepath, 'w') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows([r.data for r in self.records])


class JSONLoader:
    """
    Load data to JSON file.
    """
    
    def __init__(self, filepath: str, pretty: bool = True):
        self.filepath = filepath
        self.pretty = pretty
        self.records: List[DataRecord] = []
    
    def load(self, record: DataRecord) -> None:
        """
        Add record to buffer.
        """
        self.records.append(record)
    
    def save(self) -> None:
        """
        Write all records to JSON file.
        """
        Path(self.filepath).parent.mkdir(parents=True, exist_ok=True)
        data = [r.data for r in self.records]
        with open(self.filepath, 'w') as f:
            if self.pretty:
                json.dump(data, f, indent=2)
            else:
                json.dump(data, f, indent=None)

